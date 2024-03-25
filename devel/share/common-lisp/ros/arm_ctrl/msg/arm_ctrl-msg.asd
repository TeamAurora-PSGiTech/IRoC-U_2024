
(cl:in-package :asdf)

(defsystem "arm_ctrl-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "arm_msg" :depends-on ("_package_arm_msg"))
    (:file "_package_arm_msg" :depends-on ("_package"))
    (:file "arm_msg" :depends-on ("_package_arm_msg"))
    (:file "_package_arm_msg" :depends-on ("_package"))
  ))