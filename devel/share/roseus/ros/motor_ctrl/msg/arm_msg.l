;; Auto-generated. Do not edit!


(when (boundp 'motor_ctrl::arm_msg)
  (if (not (find-package "MOTOR_CTRL"))
    (make-package "MOTOR_CTRL"))
  (shadow 'arm_msg (find-package "MOTOR_CTRL")))
(unless (find-package "MOTOR_CTRL::ARM_MSG")
  (make-package "MOTOR_CTRL::ARM_MSG"))

(in-package "ROS")
;;//! \htmlinclude arm_msg.msg.html


(defclass motor_ctrl::arm_msg
  :super ros::object
  :slots (_base_motor _link_1 _link_2 _link_3 _waist _claw ))

(defmethod motor_ctrl::arm_msg
  (:init
   (&key
    ((:base_motor __base_motor) 0)
    ((:link_1 __link_1) 0)
    ((:link_2 __link_2) 0)
    ((:link_3 __link_3) 0)
    ((:waist __waist) 0)
    ((:claw __claw) 0)
    )
   (send-super :init)
   (setq _base_motor (round __base_motor))
   (setq _link_1 (round __link_1))
   (setq _link_2 (round __link_2))
   (setq _link_3 (round __link_3))
   (setq _waist (round __waist))
   (setq _claw (round __claw))
   self)
  (:base_motor
   (&optional __base_motor)
   (if __base_motor (setq _base_motor __base_motor)) _base_motor)
  (:link_1
   (&optional __link_1)
   (if __link_1 (setq _link_1 __link_1)) _link_1)
  (:link_2
   (&optional __link_2)
   (if __link_2 (setq _link_2 __link_2)) _link_2)
  (:link_3
   (&optional __link_3)
   (if __link_3 (setq _link_3 __link_3)) _link_3)
  (:waist
   (&optional __waist)
   (if __waist (setq _waist __waist)) _waist)
  (:claw
   (&optional __claw)
   (if __claw (setq _claw __claw)) _claw)
  (:serialization-length
   ()
   (+
    ;; int16 _base_motor
    2
    ;; int16 _link_1
    2
    ;; int16 _link_2
    2
    ;; int16 _link_3
    2
    ;; int16 _waist
    2
    ;; int16 _claw
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _base_motor
       (write-word _base_motor s)
     ;; int16 _link_1
       (write-word _link_1 s)
     ;; int16 _link_2
       (write-word _link_2 s)
     ;; int16 _link_3
       (write-word _link_3 s)
     ;; int16 _waist
       (write-word _waist s)
     ;; int16 _claw
       (write-word _claw s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _base_motor
     (setq _base_motor (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _link_1
     (setq _link_1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _link_2
     (setq _link_2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _link_3
     (setq _link_3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _waist
     (setq _waist (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _claw
     (setq _claw (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get motor_ctrl::arm_msg :md5sum-) "b0a36bb5dec1345af28caa5406649a86")
(setf (get motor_ctrl::arm_msg :datatype-) "motor_ctrl/arm_msg")
(setf (get motor_ctrl::arm_msg :definition-)
      "int16 base_motor
int16 link_1
int16 link_2
int16 link_3
int16 waist
int16 claw
")



(provide :motor_ctrl/arm_msg "b0a36bb5dec1345af28caa5406649a86")


