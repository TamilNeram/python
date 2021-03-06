(defun init-func (fun data evt)
    (setf (textdomain) "myapp") ;; replace with the appropriate catalog name
    (defun _ (msgid) (gettext msgid "myapp"))

    (let ((appframe (make-MyAppFrame)))
    (ELJApp_SetTopWindow (slot-top-window appframe))
    (wxWindow_Show (slot-top-window appframe))))

(unwind-protect
    (Eljapp_initializeC (wxclosure_Create #'init-func nil) 0 nil)
    (ffi:close-foreign-library "../miscellaneous/wxc-msw2.6.2.dll"))
