#############################################################################
# Generated by PAGE version 4.8a
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


vTcl:font:add_GUI_font font10 \
"-family {DejaVu Sans Mono} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font font11 \
"-family {DejaVu Sans} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) #f5deb3
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#f5deb3} -highlightbackground {#f5deb3} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Canvas Example"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure Custom -background #f5deb3
    ttk::style configure Custom -foreground #000000
    ttk::style configure Custom -font font10
    vTcl::widgets::ttk::custom::CreateCmd $top.cus38 \
        -background {#f5deb3} -height 75 -highlightbackground {#f5deb3} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.cus38" "Custom1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.cus38 \
        -in $top -x 0 -y 0 -relwidth 1 -relheight 1 -anchor nw \
        -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37

