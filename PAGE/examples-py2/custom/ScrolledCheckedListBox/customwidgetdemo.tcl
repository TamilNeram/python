#############################################################################
# Generated by PAGE version 4.15a
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

vTcl:font:add_GUI_font font9 \
"-family {DejaVu Sans Mono} -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top39
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top39
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra42
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
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top39 {base} {
    if {$base == ""} {
        set base .top39
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9}
    wm focusmodel $top passive
    wm geometry $top 529x522+296+123
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1265 770
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Custom Widget Demo"
    vTcl:DefineAlias "$top" "formCustomDemo" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi40 \
        -cursor bottom_right_corner
    vTcl:DefineAlias "$top.tSi40" "TSizegrip1" vTcl:WidgetProc "formCustomDemo" 1
    message $top.mes41 \
        -background {#d9d9d9} -font font9 -foreground {#000000} \
        -highlightcolor black -relief sunken -text Message -width 491
    vTcl:DefineAlias "$top.mes41" "Message1" vTcl:WidgetProc "formCustomDemo" 1
    frame $top.fra42 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 375 \
        -width 265
    vTcl:DefineAlias "$top.fra42" "Frame1" vTcl:WidgetProc "formCustomDemo" 1
    set site_3_0 $top.fra42
    vTcl::widgets::ttk::custom::CreateCmd $site_3_0.cus46 \
        -background {#d9d9d9} -height 75 -highlightcolor black -width 125
    vTcl:DefineAlias "$site_3_0.cus46" "Custom1" vTcl:WidgetProc "formCustomDemo" 1
    place $site_3_0.cus46 \
        -in $site_3_0 -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore
    button $top.but43 \
        -activebackground {#d9d9d9} -background {#d9d9d9} \
        -command on_btnGetChecks -font font9 -foreground {#000000} \
        -highlightcolor black -text {Get Checks}
    vTcl:DefineAlias "$top.but43" "btnGetChecks" vTcl:WidgetProc "formCustomDemo" 1
    button $top.but44 \
        -activebackground {#d9d9d9} -background {#d9d9d9} \
        -command on_btnClearChecks -font font9 -foreground {#000000} \
        -highlightcolor black -text {Clear Checks}
    vTcl:DefineAlias "$top.but44" "btnClearChecks" vTcl:WidgetProc "formCustomDemo" 1
    button $top.but45 \
        -activebackground {#d9d9d9} -background {#d9d9d9} -command on_btnExit \
        -font font9 -foreground {#000000} -highlightcolor black -text Exit
    vTcl:DefineAlias "$top.but45" "btnExit" vTcl:WidgetProc "formCustomDemo" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tSi40 \
        -in $top -x 0 -relx 1 -y 0 -rely 1 -anchor se -bordermode inside
    place $top.mes41 \
        -in $top -x 20 -y 15 -width 491 -relwidth 0 -height 63 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.fra42 \
        -in $top -x 30 -y 110 -width 265 -relwidth 0 -height 375 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.but43 \
        -in $top -x 360 -y 175 -width 110 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.but44 \
        -in $top -x 360 -y 275 -width 110 -height 30 -anchor nw \
        -bordermode ignore
    place $top.but45 \
        -in $top -x 360 -y 375 -width 110 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore

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

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top39 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

