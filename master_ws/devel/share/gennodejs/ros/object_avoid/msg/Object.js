// Auto-generated. Do not edit!

// (in-package object_avoid.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.front = null;
      this.left = null;
      this.right = null;
      this.left2 = null;
      this.right2 = null;
    }
    else {
      if (initObj.hasOwnProperty('front')) {
        this.front = initObj.front
      }
      else {
        this.front = 0;
      }
      if (initObj.hasOwnProperty('left')) {
        this.left = initObj.left
      }
      else {
        this.left = 0;
      }
      if (initObj.hasOwnProperty('right')) {
        this.right = initObj.right
      }
      else {
        this.right = 0;
      }
      if (initObj.hasOwnProperty('left2')) {
        this.left2 = initObj.left2
      }
      else {
        this.left2 = 0;
      }
      if (initObj.hasOwnProperty('right2')) {
        this.right2 = initObj.right2
      }
      else {
        this.right2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Object
    // Serialize message field [front]
    bufferOffset = _serializer.int32(obj.front, buffer, bufferOffset);
    // Serialize message field [left]
    bufferOffset = _serializer.int32(obj.left, buffer, bufferOffset);
    // Serialize message field [right]
    bufferOffset = _serializer.int32(obj.right, buffer, bufferOffset);
    // Serialize message field [left2]
    bufferOffset = _serializer.int32(obj.left2, buffer, bufferOffset);
    // Serialize message field [right2]
    bufferOffset = _serializer.int32(obj.right2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Object
    let len;
    let data = new Object(null);
    // Deserialize message field [front]
    data.front = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [left]
    data.left = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [right]
    data.right = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [left2]
    data.left2 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [right2]
    data.right2 = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_avoid/Object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f0581ce5ecc11cefc11e361045e60699';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 front
    int32 left
    int32 right
    int32 left2
    int32 right2
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Object(null);
    if (msg.front !== undefined) {
      resolved.front = msg.front;
    }
    else {
      resolved.front = 0
    }

    if (msg.left !== undefined) {
      resolved.left = msg.left;
    }
    else {
      resolved.left = 0
    }

    if (msg.right !== undefined) {
      resolved.right = msg.right;
    }
    else {
      resolved.right = 0
    }

    if (msg.left2 !== undefined) {
      resolved.left2 = msg.left2;
    }
    else {
      resolved.left2 = 0
    }

    if (msg.right2 !== undefined) {
      resolved.right2 = msg.right2;
    }
    else {
      resolved.right2 = 0
    }

    return resolved;
    }
};

module.exports = Object;
