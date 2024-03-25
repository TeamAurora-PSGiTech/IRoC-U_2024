// Auto-generated. Do not edit!

// (in-package arm_ctrl.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class arm_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.base_motor = null;
      this.link_1 = null;
      this.link_2 = null;
      this.link_3 = null;
      this.waist = null;
      this.claw = null;
    }
    else {
      if (initObj.hasOwnProperty('base_motor')) {
        this.base_motor = initObj.base_motor
      }
      else {
        this.base_motor = 0;
      }
      if (initObj.hasOwnProperty('link_1')) {
        this.link_1 = initObj.link_1
      }
      else {
        this.link_1 = 0;
      }
      if (initObj.hasOwnProperty('link_2')) {
        this.link_2 = initObj.link_2
      }
      else {
        this.link_2 = 0;
      }
      if (initObj.hasOwnProperty('link_3')) {
        this.link_3 = initObj.link_3
      }
      else {
        this.link_3 = 0;
      }
      if (initObj.hasOwnProperty('waist')) {
        this.waist = initObj.waist
      }
      else {
        this.waist = 0;
      }
      if (initObj.hasOwnProperty('claw')) {
        this.claw = initObj.claw
      }
      else {
        this.claw = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type arm_msg
    // Serialize message field [base_motor]
    bufferOffset = _serializer.int16(obj.base_motor, buffer, bufferOffset);
    // Serialize message field [link_1]
    bufferOffset = _serializer.int16(obj.link_1, buffer, bufferOffset);
    // Serialize message field [link_2]
    bufferOffset = _serializer.int16(obj.link_2, buffer, bufferOffset);
    // Serialize message field [link_3]
    bufferOffset = _serializer.int16(obj.link_3, buffer, bufferOffset);
    // Serialize message field [waist]
    bufferOffset = _serializer.int16(obj.waist, buffer, bufferOffset);
    // Serialize message field [claw]
    bufferOffset = _serializer.int16(obj.claw, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type arm_msg
    let len;
    let data = new arm_msg(null);
    // Deserialize message field [base_motor]
    data.base_motor = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [link_1]
    data.link_1 = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [link_2]
    data.link_2 = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [link_3]
    data.link_3 = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [waist]
    data.waist = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [claw]
    data.claw = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'arm_ctrl/arm_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b0a36bb5dec1345af28caa5406649a86';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 base_motor
    int16 link_1
    int16 link_2
    int16 link_3
    int16 waist
    int16 claw
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new arm_msg(null);
    if (msg.base_motor !== undefined) {
      resolved.base_motor = msg.base_motor;
    }
    else {
      resolved.base_motor = 0
    }

    if (msg.link_1 !== undefined) {
      resolved.link_1 = msg.link_1;
    }
    else {
      resolved.link_1 = 0
    }

    if (msg.link_2 !== undefined) {
      resolved.link_2 = msg.link_2;
    }
    else {
      resolved.link_2 = 0
    }

    if (msg.link_3 !== undefined) {
      resolved.link_3 = msg.link_3;
    }
    else {
      resolved.link_3 = 0
    }

    if (msg.waist !== undefined) {
      resolved.waist = msg.waist;
    }
    else {
      resolved.waist = 0
    }

    if (msg.claw !== undefined) {
      resolved.claw = msg.claw;
    }
    else {
      resolved.claw = 0
    }

    return resolved;
    }
};

module.exports = arm_msg;
