#!/usr/bin/env python
"""
AntAPI.py
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

class AntAPI(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def CreateAnnotation(self, userId, fileId, postData, ):
        """Create annotation
        Args:
            userId -- User GUID
            fileId -- File ID
            postData -- annotation

        Return:
            CreateAnnotationResponse -- an instance of CreateAnnotationResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/files/{fileId}/annotations'
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
                                          postData, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'CreateAnnotationResponse')
        return responseObject


    def ListAnnotations(self, userId, fileId, ):
        """Get list of annotations
        Args:
            userId -- User GUID
            fileId -- File ID

        Return:
            ListAnnotationsResponse -- an instance of ListAnnotationsResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/files/{fileId}/annotations'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

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
                                                    'ListAnnotationsResponse')
        return responseObject


    def DeleteAnnotation(self, userId, annotationId, ):
        """Delete annotation
        Args:
            userId -- User GUID
            annotationId -- Annotation ID

        Return:
            DeleteAnnotationResponse -- an instance of DeleteAnnotationResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/annotations/{annotationId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if annotationId != None:
            resourcePath = resourcePath.replace('{annotationId}', annotationId)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'DeleteAnnotationResponse')
        return responseObject


    def CreateAnnotationReply(self, userId, annotationId, message, ):
        """Create annotation reply
        Args:
            userId -- User GUID
            annotationId -- Annotation ID
            message -- Message

        Return:
            AddReplyResponse -- an instance of AddReplyResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/annotations/{annotationId}/replies'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'POST'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if annotationId != None:
            resourcePath = resourcePath.replace('{annotationId}', annotationId)
        if message != None:
            resourcePath = resourcePath.replace('{message}', message)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'AddReplyResponse')
        return responseObject


    def EditAnnotationReply(self, userId, replyGuid, message, ):
        """Edit annotation reply
        Args:
            userId -- User GUID
            replyGuid -- Reply GUID
            message -- Message

        Return:
            EditReplyResponse -- an instance of EditReplyResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/replies/{replyGuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'PUT'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if replyGuid != None:
            resourcePath = resourcePath.replace('{replyGuid}', replyGuid)
        if message != None:
            resourcePath = resourcePath.replace('{message}', message)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'EditReplyResponse')
        return responseObject


    def ListAnnotationReplies(self, userId, annotationId, after, ):
        """Get list of annotation replies
        Args:
            userId -- User GUID
            annotationId -- Annotation ID
            after -- After

        Return:
            ListRepliesResponse -- an instance of ListRepliesResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/annotations/{annotationId}/replies?after={after}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if annotationId != None:
            resourcePath = resourcePath.replace('{annotationId}', annotationId)
        if after != None:
            resourcePath = resourcePath.replace('{after}', after)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'ListRepliesResponse')
        return responseObject


    def SetAnnotationCollaborators(self, userId, fileId, collaborators, ):
        """Set annotation collaborators
        Args:
            userId -- User GUID
            fileId -- File ID
            collaborators -- Collaborators

        Return:
            SetCollaboratorsResponse -- an instance of SetCollaboratorsResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/files/{fileId}/collaborators'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'PUT'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if fileId != None:
            resourcePath = resourcePath.replace('{fileId}', fileId)
        if collaborators != None:
            resourcePath = resourcePath.replace('{collaborators}', collaborators)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'SetCollaboratorsResponse')
        return responseObject


    def GetAnnotationCollaborators(self, userId, fileId, ):
        """Get list of annotation collaborators
        Args:
            userId -- User GUID
            fileId -- File ID

        Return:
            GetCollaboratorsResponse -- an instance of GetCollaboratorsResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/files/{fileId}/collaborators'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

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
                                                    'GetCollaboratorsResponse')
        return responseObject


    def MoveAnnotation(self, userId, annotationId, postData, ):
        """Move annotation
        Args:
            userId -- User GUID
            annotationId -- Annotation ID
            postData -- position

        Return:
            MoveAnnotationResponse -- an instance of MoveAnnotationResponse"""

        # Parse inputs
        resourcePath = '/ant/{userId}/annotations/{annotationId}/position'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'PUT'

        queryParams = {}
        headerParams = {}


        if userId != None:
            resourcePath = resourcePath.replace('{userId}', userId)
        if annotationId != None:
            resourcePath = resourcePath.replace('{annotationId}', annotationId)


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'MoveAnnotationResponse')
        return responseObject

