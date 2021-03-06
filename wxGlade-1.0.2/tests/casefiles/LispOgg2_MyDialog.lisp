;;; generated by wxGlade "faked test version"
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxButton)
(use-package :wxCL)
(use-package :wxCheckBox)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxNotebook)
(use-package :wxPanel)
(use-package :wxRadioBox)
(use-package :wxSizer)
(use-package :wxStaticLine)
(use-package :wxStaticText)
(use-package :wxTextCtrl)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; useless extra code for LispOgg2_MyDialog
;;; end wxGlade


(defclass LispOgg2_MyDialog()
        ((top-window :initform nil :accessor slot-top-window)
        (label-1 :initform nil :accessor slot-label-1)
        (text-ctrl-1 :initform nil :accessor slot-text-ctrl-1)
        (button-3 :initform nil :accessor slot-button-3)
        (grid-sizer-1 :initform nil :accessor slot-grid-sizer-1)
        (notebook-1-pane-1 :initform nil :accessor slot-notebook-1-pane-1)
        (radio-box-1 :initform nil :accessor slot-radio-box-1)
        (sizer-4 :initform nil :accessor slot-sizer-4)
        (notebook-1-pane-2 :initform nil :accessor slot-notebook-1-pane-2)
        (text-ctrl-2 :initform nil :accessor slot-text-ctrl-2)
        (sizer-3 :initform nil :accessor slot-sizer-3)
        (notebook-1-pane-3 :initform nil :accessor slot-notebook-1-pane-3)
        (label-2 :initform nil :accessor slot-label-2)
        (text-ctrl-3 :initform nil :accessor slot-text-ctrl-3)
        (button-4 :initform nil :accessor slot-button-4)
        (checkbox-1 :initform nil :accessor slot-checkbox-1)
        (grid-sizer-2 :initform nil :accessor slot-grid-sizer-2)
        (notebook-1-pane-4 :initform nil :accessor slot-notebook-1-pane-4)
        (notebook-1 :initform nil :accessor slot-notebook-1)
        (static-line-1 :initform nil :accessor slot-static-line-1)
        (button-5 :initform nil :accessor slot-button-5)
        (button-2 :initform nil :accessor slot-button-2)
        (button-1 :initform nil :accessor slot-button-1)
        (sizer-2 :initform nil :accessor slot-sizer-2)
        (sizer-1 :initform nil :accessor slot-sizer-1)))

(defun make-LispOgg2_MyDialog ()
        (let ((obj (make-instance 'LispOgg2_MyDialog)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj LispOgg2_MyDialog))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: LispOgg2_MyDialog.__init__
        (setf (slot-top-window obj) (wxDialog_create nil wxID_ANY "" -1 -1 -1 -1 (logior wxDEFAULT_DIALOG_STYLE wxRESIZE_BORDER)))
        (slot-top-window obj).wxWindow_SetSize((500, 300))
        (wxWindow_SetTitle (slot-Mp3-To-Ogg self) (_"mp3 2 ogg"))
        
        (setf (slot-sizer-1 obj) (wxGridSizer_Create 3 1 0 0))
        
        (setf (slot-notebook-1 obj) (wxNotebook_Create (slot-top-window obj) wxID_ANY -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-notebook-1 obj) 1 wxEXPAND 0 nil)
        
        (setf (slot-notebook-1-pane-1 obj) (wxPanel_Create (slot-notebook-1 obj) wxID_ANY -1 -1 -1 -1 wxTAB_TRAVERSAL))
        (wxNotebook_AddPage (slot-notebook-1 obj) (slot-notebook-1-pane-1 obj) (_"Input File") 1 -1)
        
        (setf (slot-grid-sizer-1 obj) (wxGridSizer_Create 1 3 0 0))
        
        (setf (slot-label-1 obj) (wxStaticText_Create (slot-notebook-1-pane-1 obj) wxID_ANY (_"File name:") -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-1 obj) (slot-label-1 obj) 0 (logior wxALIGN_CENTER_VERTICAL wxALL) 5 nil)
        
        (setf (slot-text-ctrl-1 obj) (wxTextCtrl_Create (slot-notebook-1-pane-1 obj) wxID_ANY "" -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-1 obj) (slot-text-ctrl-1 obj) 1 (logior wxALIGN_CENTER_VERTICAL wxALL wxEXPAND) 5 nil)
        
        (setf (slot-button-3 obj) (wxButton_Create (slot-notebook-1-pane-1 obj) wxID_OPEN "" -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-1 obj) (slot-button-3 obj) 0 wxALL 5 nil)
        
        (setf (slot-notebook-1-pane-2 obj) (wxPanel_Create (slot-notebook-1 obj) wxID_ANY -1 -1 -1 -1 wxTAB_TRAVERSAL))
        (wxNotebook_AddPage (slot-notebook-1 obj) (slot-notebook-1-pane-2 obj) (_"Converting Options") 1 -1)
        
        (setf (slot-sizer-4 obj) (wxBoxSizer_Create wxHORIZONTAL))
        
        (setf (slot-radio-box-1 obj) (wxRadioBox_Create (slot-notebook-1-pane-2 obj) wxID_ANY (_"Sampling Rate") -1 -1 -1 -1 2 (vector (_"44 kbit") (_"128 kbit")) 0 wxRA_SPECIFY_ROWS))
        (wxRadioBox_SetSelection (slot-radio-box-1 obj) 0)
        (wxSizer_AddWindow (slot-sizer-4 obj) (slot-radio-box-1 obj) 0 (logior wxALL wxEXPAND wxSHAPED) 5 nil)
        
        (setf (slot-notebook-1-pane-3 obj) (wxPanel_Create (slot-notebook-1 obj) wxID_ANY -1 -1 -1 -1 wxTAB_TRAVERSAL))
        (wxNotebook_AddPage (slot-notebook-1 obj) (slot-notebook-1-pane-3 obj) (_"Converting Progress") 1 -1)
        
        (setf (slot-sizer-3 obj) (wxBoxSizer_Create wxHORIZONTAL))
        
        (setf (slot-text-ctrl-2 obj) (wxTextCtrl_Create (slot-notebook-1-pane-3 obj) wxID_ANY "" -1 -1 -1 -1 wxTE_MULTILINE))
        (wxSizer_AddWindow (slot-sizer-3 obj) (slot-text-ctrl-2 obj) 1 (logior wxALL wxEXPAND) 5 nil)
        
        (setf (slot-notebook-1-pane-4 obj) (wxPanel_Create (slot-notebook-1 obj) wxID_ANY -1 -1 -1 -1 wxTAB_TRAVERSAL))
        (wxNotebook_AddPage (slot-notebook-1 obj) (slot-notebook-1-pane-4 obj) (_"Output File") 1 -1)
        
        (setf (slot-grid-sizer-2 obj) (wxGridSizer_Create 2 3 0 0))
        
        (setf (slot-label-2 obj) (wxStaticText_Create (slot-notebook-1-pane-4 obj) wxID_ANY (_"File name:") -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) (slot-label-2 obj) 0 (logior wxALIGN_CENTER_VERTICAL wxALL) 5 nil)
        
        (setf (slot-text-ctrl-3 obj) (wxTextCtrl_Create (slot-notebook-1-pane-4 obj) wxID_ANY "" -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) (slot-text-ctrl-3 obj) 0 (logior wxALL wxEXPAND) 5 nil)
        
        (setf (slot-button-4 obj) (wxButton_Create (slot-notebook-1-pane-4 obj) wxID_OPEN "" -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) (slot-button-4 obj) 0 wxALL 5 nil)
        
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) ((20, 20) obj) 0 0 0 nil)
        
        (setf (slot-checkbox-1 obj) (wxCheckBox_Create (slot-notebook-1-pane-4 obj) wxID_ANY (_"Overwrite existing file") -1 -1 -1 -1 0))
        (wxWindow_SetToolTip (slot-checkbox-1 obj)(_"Overwrite an existing file"))
        (wxCheckBox_SetValue (slot-checkbox-1 obj) 1)
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) (slot-checkbox-1 obj) 0 (logior wxALL wxEXPAND) 5 nil)
        
        (wxSizer_AddWindow (slot-grid-sizer-2 obj) ((20, 20) obj) 0 0 0 nil)
        
        (setf (slot-static-line-1 obj) (wxStaticLine_Create (slot-top-window obj) wxID_ANY -1 -1 -1 -1 wxLI_HORIZONTAL))
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-static-line-1 obj) 0 (logior wxALL wxEXPAND) 5 nil)
        
        (setf (slot-sizer-2 obj) (wxGridSizer_Create 1 3 0 0))
        (wxSizer_AddSizer (slot-sizer-1 obj) (slot-sizer-2 obj) 0 wxALIGN_RIGHT 0 nil)
        
        (setf (slot-button-5 obj) (wxButton_Create (slot-top-window obj) wxID_CLOSE "" -1 -1 -1 -1 0))
        (wxSizer_AddWindow (slot-sizer-2 obj) (slot-button-5 obj) 0 (logior wxALIGN_RIGHT wxALL) 5 nil)
        
        (setf (slot-button-2 obj) (wxButton_Create (slot-top-window obj) wxID_CANCEL "" -1 -1 -1 -1 wxBU_TOP))
        (wxSizer_AddWindow (slot-sizer-2 obj) (slot-button-2 obj) 0 (logior wxALIGN_RIGHT wxALL) 5 nil)
        
        (setf (slot-button-1 obj) (wxButton_Create (slot-top-window obj) wxID_OK "" -1 -1 -1 -1 wxBU_TOP))
        (wxSizer_AddWindow (slot-sizer-2 obj) (slot-button-1 obj) 0 (logior wxALIGN_RIGHT wxALL) 5 nil)
        
        (wxFlexGridSizer_AddGrowableCol (slot-grid-sizer-2 obj) 1)
        (wxWindow_SetSizer (slot-notebook-1-pane-4 obj) (slot-grid-sizer-2 obj))
        
        (wxWindow_SetSizer (slot-notebook-1-pane-3 obj) (slot-sizer-3 obj))
        
        (wxWindow_SetSizer (slot-notebook-1-pane-2 obj) (slot-sizer-4 obj))
        
        (wxFlexGridSizer_AddGrowableCol (slot-grid-sizer-1 obj) 1)
        (wxWindow_SetSizer (slot-notebook-1-pane-1 obj) (slot-grid-sizer-1 obj))
        
        (wxFlexGridSizer_AddGrowableRow (slot-sizer-1 obj) 0)
        (wxFlexGridSizer_AddGrowableCol (slot-sizer-1 obj) 0)
        (wxWindow_SetSizer (slot-frame obj) (slot-sizer-1 obj))
        
        (wxWindow_layout (slot-Mp3-To-Ogg self))
        (wxWindow_Centre (slot-Mp3-To-Ogg self) wxBOTH)

        (wxEvtHandler_Connect (slot-top-window obj) obj.button-1 (expwxEVT_BUTTON)
        (wxClosure_Create #'startConverting obj))
        ;;; end wxGlade
        )

(defmethod set-properties ((obj LispOgg2_MyDialog))
        )

(defmethod do-layout ((obj LispOgg2_MyDialog))
        )

(defun startConverting (function data event) ;;; wxGlade: LispOgg2_MyDialog.<event_handler>
        (print "Event handler 'startConverting' not implemented!")
        (when event
                (wxEvent:wxEvent_Skip event)))

;;; end of class LispOgg2_MyDialog


