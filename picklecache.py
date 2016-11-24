#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""

import os

import pickle


class PickleCache(object):
    """Object that stors some data"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache class.

        Args:
            file_path(str, optional): Argument for file location. Defaults to da
            tastore.pkl.
            autosync(bool, optional): Defaults to False.

        Attributes:
            file_path(str, optional): Argument for file location. Defaults to da
            tastore.pkl.
            autosync(bool, optional): Defaults to False.
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Function does some dictionary operation.

        Args:
            key(mixed): User input.
            value(mixed): User input.

        Returns
            dict: Filled dictionary.

        Examples:

            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data.update({key: value})
        if self.autosync:
            self.flush()

    def __len__(self):
        """Function does some math.

        Args:
            No arguments.

        Returns:
            int: The length of self.__data.

        Examples:

            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """Function to check for error.

        Args:
            key(mixed): Key input.

        Returns:
            mixed: Dictionry value or KeyError message if input is incorrect.

        Examples:

            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        if self.__data[key] and not None:
            return self.__data[key]
        else:
            raise KeyError('KeyError')

    def __delitem__(self, key):
        """Function to delete an item.

        Args:
            key(mixed): Dictionary key.

        Returns:
            int: Number of deleted keys.

        Examples:

            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """Function to load file objects.

         Args:
            No arguments.

        Returns:
            str: Loaded data.

        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """

        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            f_han = open(self.__file_path, 'r')
            self.__data = pickle.load(f_han)
        else:
            return False
        f_han.close()

    def flush(self):
        """Function to write data.

         Args:
            No arguments.

        Returns:
            dict: Written dictionary.

        Examples:

            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        new = open(self.__file_path, 'w')
        pickle.dump(self.__data, new)
        new.close()
