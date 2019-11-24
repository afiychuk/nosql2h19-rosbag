#! /usr/bin/env python
# -*- coding: utf-8 -*-s
from pymongo import MongoClient
import datetime
from pprint import pprint


class dbQueryManager(object):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(dbQueryManager, self).__new__(self)
        return self.instance
    '''
    В конструктор передаётся название коллекции и базы данных (опционально).
    '''
    def __init__(self, db_name="test_database"):
        self.client = MongoClient()
        self.db = self.client[db_name]


    def getNumberOfDocuments(self, collection_name):
        collection = self.db[collection_name]
        result = collection.count({})
        # result = 3
        return result

    def getDocumentNames(self, collection_name):
        result = ["Name1", "Name2", "Name3"]
        return result

    def getMainInfo(self, collection_name):
        collection = self.db[collection_name]
        resultCursor = collection.find({}, {"topics_list.msgs_list.msgs" : {"$slice": 10}})

        # {ObjectId('5dd9b9f36596cd0075468968'): {u'duration': 0.599675178527832, u'topics_list': [{u'msgs_type': u'geometry_msgs/Quaternion', u'msgs_list': [{u'msg_name': u'x', u'msg_type': u'float64', u'msgs': [u'10.0', u'10.0', u'10.0', u'10.0']}, {u'msg_name': u'y', u'msg_type': u'float64', u'msgs': [u'50.0', u'33.3333333333', u'25.0', u'20.0']}, {u'msg_name': u'z', u'msg_type': u'float64', u'msgs': [u'11.0', u'12.0', u'13.0', u'14.0']}, {u'msg_name': u'w', u'msg_type': u'float64', u'msgs': [u'22.2', u'22.2', u'22.2', u'22.2']}], u'topic_name': u'quaternionTopic', u'msgs_num': 4}, {u'msgs_type': u'geometry_msgs/Pose', u'msgs_list': [{u'msg_name': u'position/x', u'msg_type': u'geometry_msgs/Point/float64', u'msgs': [u'1.1', u'1.1', u'1.1', u'1.1']}, {u'msg_name': u'position/y', u'msg_type': u'geometry_msgs/Point/float64', u'msgs': [u'2.2', u'2.2', u'2.2', u'2.2']}, {u'msg_name': u'position/z', u'msg_type': u'geometry_msgs/Point/float64', u'msgs': [u'3.3', u'3.3', u'3.3', u'3.3']}, {u'msg_name': u'orientation/x', u'msg_type': u'geometry_msgs/Quaternion/float64', u'msgs': [u'11.1', u'12.1', u'13.1', u'14.1']}, {u'msg_name': u'orientation/y', u'msg_type': u'geometry_msgs/Quaternion/float64', u'msgs': [u'13.1', u'14.1', u'15.1', u'16.1']}, {u'msg_name': u'orientation/z', u'msg_type': u'geometry_msgs/Quaternion/float64', u'msgs': [u'24.1', u'25.1', u'26.1', u'27.1']}, {u'msg_name': u'orientation/w', u'msg_type': u'geometry_msgs/Quaternion/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0']}], u'topic_name': u'poseTopic', u'msgs_num': 4}], u'date_creation': datetime.datetime(2019, 11, 9, 2, 12, 40, 148000), u'filename': u'Double.bag'}, ObjectId('5dd9ba5d43e8c2ce48323718'): {u'duration': 10.599474668502808, u'topics_list': [{u'msgs_type': u'std_msgs/String', u'msgs_list': [{u'msg_name': u'data', u'msg_type': u'string', u'msgs': [u'"hello world 1573044926.85"', u'"hello world 1573044926.95"', u'"hello world 1573044927.05"', u'"hello world 1573044927.15"', u'"hello world 1573044927.25"', u'"hello world 1573044927.35"', u'"hello world 1573044927.45"', u'"hello world 1573044927.55"', u'"hello world 1573044927.65"', u'"hello world 1573044927.75"']}], u'topic_name': u'/chatter', u'msgs_num': 107}], u'date_creation': datetime.datetime(2019, 11, 6, 15, 55, 26, 848000), u'filename': u'hello.bag'}, ObjectId('5dd9ba53601fe822faaeda5b'): {u'duration': 29.82285976409912, u'topics_list': [{u'msgs_type': u'geometry_msgs/Twist', u'msgs_list': [{u'msg_name': u'linear/x', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'2.0', u'2.0', u'2.0', u'2.0', u'2.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0']}, {u'msg_name': u'linear/y', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0']}, {u'msg_name': u'linear/z', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0']}, {u'msg_name': u'angular/x', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0']}, {u'msg_name': u'angular/y', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'0.0']}, {u'msg_name': u'angular/z', u'msg_type': u'geometry_msgs/Vector3/float64', u'msgs': [u'0.0', u'0.0', u'0.0', u'0.0', u'0.0', u'-2.0', u'-2.0', u'-2.0', u'-2.0', u'-2.0']}], u'topic_name': u'/turtle1/cmd_vel', u'msgs_num': 325}], u'date_creation': datetime.datetime(2019, 11, 6, 15, 9, 28, 982000), u'filename': u'square.bag'}}
        return dbQueryManager.__cursorToMap(resultCursor)

    def getSortedBy(self, collection_name, sortedKey):
        collection = self.db[collection_name]
        resultCursor = collection.find().sort(
            [(sortedKey, 1)]
        )
        return dbQueryManager.__cursorToMap(resultCursor)


    @staticmethod
    def __cursorToMap(iterableOfMaps):
        returned = {}
        for obj in iterableOfMaps:
            objID = obj.pop("_id")
            returned[objID] = obj
        return returned



if __name__ == "__main__":
    manager = dbQueryManager()
    collection = "bagfiles_test"
    
    manager.getNumberOfDocuments(collection)
    manager.getDocumentNames(collection)
    
    listOfBags = manager.getMainInfo(collection)
    print(listOfBags)
    # kek = manager.getSortedBy(collection, "date_creation")
    # kek = [elem["_id"] for elem in kek]
    # print(kek)
    

