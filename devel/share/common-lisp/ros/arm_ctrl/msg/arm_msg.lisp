; Auto-generated. Do not edit!


(cl:in-package arm_ctrl-msg)


;//! \htmlinclude arm_msg.msg.html

(cl:defclass <arm_msg> (roslisp-msg-protocol:ros-message)
  ((base_motor
    :reader base_motor
    :initarg :base_motor
    :type cl:fixnum
    :initform 0)
   (link_1
    :reader link_1
    :initarg :link_1
    :type cl:fixnum
    :initform 0)
   (link_2
    :reader link_2
    :initarg :link_2
    :type cl:fixnum
    :initform 0)
   (link_3
    :reader link_3
    :initarg :link_3
    :type cl:fixnum
    :initform 0)
   (waist
    :reader waist
    :initarg :waist
    :type cl:fixnum
    :initform 0)
   (claw
    :reader claw
    :initarg :claw
    :type cl:fixnum
    :initform 0))
)

(cl:defclass arm_msg (<arm_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <arm_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'arm_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arm_ctrl-msg:<arm_msg> is deprecated: use arm_ctrl-msg:arm_msg instead.")))

(cl:ensure-generic-function 'base_motor-val :lambda-list '(m))
(cl:defmethod base_motor-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:base_motor-val is deprecated.  Use arm_ctrl-msg:base_motor instead.")
  (base_motor m))

(cl:ensure-generic-function 'link_1-val :lambda-list '(m))
(cl:defmethod link_1-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:link_1-val is deprecated.  Use arm_ctrl-msg:link_1 instead.")
  (link_1 m))

(cl:ensure-generic-function 'link_2-val :lambda-list '(m))
(cl:defmethod link_2-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:link_2-val is deprecated.  Use arm_ctrl-msg:link_2 instead.")
  (link_2 m))

(cl:ensure-generic-function 'link_3-val :lambda-list '(m))
(cl:defmethod link_3-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:link_3-val is deprecated.  Use arm_ctrl-msg:link_3 instead.")
  (link_3 m))

(cl:ensure-generic-function 'waist-val :lambda-list '(m))
(cl:defmethod waist-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:waist-val is deprecated.  Use arm_ctrl-msg:waist instead.")
  (waist m))

(cl:ensure-generic-function 'claw-val :lambda-list '(m))
(cl:defmethod claw-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_ctrl-msg:claw-val is deprecated.  Use arm_ctrl-msg:claw instead.")
  (claw m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <arm_msg>) ostream)
  "Serializes a message object of type '<arm_msg>"
  (cl:let* ((signed (cl:slot-value msg 'base_motor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'link_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'link_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'link_3)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'waist)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'claw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <arm_msg>) istream)
  "Deserializes a message object of type '<arm_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'base_motor) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'link_1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'link_2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'link_3) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'waist) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'claw) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<arm_msg>)))
  "Returns string type for a message object of type '<arm_msg>"
  "arm_ctrl/arm_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'arm_msg)))
  "Returns string type for a message object of type 'arm_msg"
  "arm_ctrl/arm_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<arm_msg>)))
  "Returns md5sum for a message object of type '<arm_msg>"
  "b0a36bb5dec1345af28caa5406649a86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'arm_msg)))
  "Returns md5sum for a message object of type 'arm_msg"
  "b0a36bb5dec1345af28caa5406649a86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<arm_msg>)))
  "Returns full string definition for message of type '<arm_msg>"
  (cl:format cl:nil "int16 base_motor~%int16 link_1~%int16 link_2~%int16 link_3~%int16 waist~%int16 claw~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'arm_msg)))
  "Returns full string definition for message of type 'arm_msg"
  (cl:format cl:nil "int16 base_motor~%int16 link_1~%int16 link_2~%int16 link_3~%int16 waist~%int16 claw~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <arm_msg>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <arm_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'arm_msg
    (cl:cons ':base_motor (base_motor msg))
    (cl:cons ':link_1 (link_1 msg))
    (cl:cons ':link_2 (link_2 msg))
    (cl:cons ':link_3 (link_3 msg))
    (cl:cons ':waist (waist msg))
    (cl:cons ':claw (claw msg))
))
