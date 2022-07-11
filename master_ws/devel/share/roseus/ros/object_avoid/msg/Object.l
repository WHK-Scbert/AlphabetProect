;; Auto-generated. Do not edit!


(when (boundp 'object_avoid::Object)
  (if (not (find-package "OBJECT_AVOID"))
    (make-package "OBJECT_AVOID"))
  (shadow 'Object (find-package "OBJECT_AVOID")))
(unless (find-package "OBJECT_AVOID::OBJECT")
  (make-package "OBJECT_AVOID::OBJECT"))

(in-package "ROS")
;;//! \htmlinclude Object.msg.html


(defclass object_avoid::Object
  :super ros::object
  :slots (_front _left _right _left2 _right2 ))

(defmethod object_avoid::Object
  (:init
   (&key
    ((:front __front) 0)
    ((:left __left) 0)
    ((:right __right) 0)
    ((:left2 __left2) 0)
    ((:right2 __right2) 0)
    )
   (send-super :init)
   (setq _front (round __front))
   (setq _left (round __left))
   (setq _right (round __right))
   (setq _left2 (round __left2))
   (setq _right2 (round __right2))
   self)
  (:front
   (&optional __front)
   (if __front (setq _front __front)) _front)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:left2
   (&optional __left2)
   (if __left2 (setq _left2 __left2)) _left2)
  (:right2
   (&optional __right2)
   (if __right2 (setq _right2 __right2)) _right2)
  (:serialization-length
   ()
   (+
    ;; int32 _front
    4
    ;; int32 _left
    4
    ;; int32 _right
    4
    ;; int32 _left2
    4
    ;; int32 _right2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _front
       (write-long _front s)
     ;; int32 _left
       (write-long _left s)
     ;; int32 _right
       (write-long _right s)
     ;; int32 _left2
       (write-long _left2 s)
     ;; int32 _right2
       (write-long _right2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _front
     (setq _front (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _left
     (setq _left (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _right
     (setq _right (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _left2
     (setq _left2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _right2
     (setq _right2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get object_avoid::Object :md5sum-) "f0581ce5ecc11cefc11e361045e60699")
(setf (get object_avoid::Object :datatype-) "object_avoid/Object")
(setf (get object_avoid::Object :definition-)
      "int32 front
int32 left
int32 right
int32 left2
int32 right2

")



(provide :object_avoid/Object "f0581ce5ecc11cefc11e361045e60699")


