#!/usr/bin/env python
"""
PostAPI.py
Copyright 2011 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import model

class PostAPI(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def RenameByPost(self, userId, fileId, newName, ):
        """Rename by post
        Args:
            userId -- User GUID
            fileId -- File GUID
            newName -- New name

        Return:
            RenameResponse -- an instance of RenameResponse"""

        # Parse inputs
        resourcePath = '/post/file.rename?user_id={userId}&file_id={fileId}&new_name={newName}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'POST'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if fileId != None:
            resourcePath = resourcePath.replace('{fileId}', fileId)
        if newName != None:
            resourcePath = resourcePath.replace('{newName}', newName)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'RenameResponse')
        return responseObject


    def DeleteByPost(self, userId, fileId, ):
        """Delete by post
        Args:
            userId -- User GUID
            fileId -- File GUID

        Return:
            DeleteResponse -- an instance of DeleteResponse"""

        # Parse inputs
        resourcePath = '/post/file.delete?user_id={userId}&file_id={fileId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'POST'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if fileId != None:
            resourcePath = resourcePath.replace('{fileId}', fileId)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'DeleteResponse')
        return responseObject


    def DeleteFromFolderByPost(self, userId, path, ):
        """Delete from folder by post
        Args:
            userId -- User GUID
            path -- Path

        Return:
            DeleteResponse -- an instance of DeleteResponse"""

        # Parse inputs
        resourcePath = '/post/file.delete.in?user_id={userId}&path={path}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'POST'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if path != None:
            resourcePath = resourcePath.replace('{path}', path)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'DeleteResponse')
        return responseObject


    def CompressByPost(self, userId, fileId, archiveType, ):
        """Compress by post
        Args:
            userId -- User GUID
            fileId -- File GUID
            archiveType -- Archive Type

        Return:
            CompressResponse -- an instance of CompressResponse"""

        # Parse inputs
        resourcePath = '/post/file.compress?user_id={userId}&file_id={fileId}&archive_type={archiveType}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'POST'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if fileId != None:
            resourcePath = resourcePath.replace('{fileId}', fileId)
        if archiveType != None:
            resourcePath = resourcePath.replace('{archiveType}', archiveType)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'CompressResponse')
        return responseObject


