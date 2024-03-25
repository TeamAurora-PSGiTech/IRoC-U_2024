# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motor_ctrl/arm_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class arm_msg(genpy.Message):
  _md5sum = "b0a36bb5dec1345af28caa5406649a86"
  _type = "motor_ctrl/arm_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int16 base_motor
int16 link_1
int16 link_2
int16 link_3
int16 waist
int16 claw"""
  __slots__ = ['base_motor','link_1','link_2','link_3','waist','claw']
  _slot_types = ['int16','int16','int16','int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       base_motor,link_1,link_2,link_3,waist,claw

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(arm_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.base_motor is None:
        self.base_motor = 0
      if self.link_1 is None:
        self.link_1 = 0
      if self.link_2 is None:
        self.link_2 = 0
      if self.link_3 is None:
        self.link_3 = 0
      if self.waist is None:
        self.waist = 0
      if self.claw is None:
        self.claw = 0
    else:
      self.base_motor = 0
      self.link_1 = 0
      self.link_2 = 0
      self.link_3 = 0
      self.waist = 0
      self.claw = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6h().pack(_x.base_motor, _x.link_1, _x.link_2, _x.link_3, _x.waist, _x.claw))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.base_motor, _x.link_1, _x.link_2, _x.link_3, _x.waist, _x.claw,) = _get_struct_6h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6h().pack(_x.base_motor, _x.link_1, _x.link_2, _x.link_3, _x.waist, _x.claw))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.base_motor, _x.link_1, _x.link_2, _x.link_3, _x.waist, _x.claw,) = _get_struct_6h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6h = None
def _get_struct_6h():
    global _struct_6h
    if _struct_6h is None:
        _struct_6h = struct.Struct("<6h")
    return _struct_6h
