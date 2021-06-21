#############################################################################
# Generated by PAGE version 5.5f
#  in conjunction with Tcl version 8.6
#  Oct 06, 2020 08:07:15 PM PDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}

set vTcl(tops) .top32


if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 12"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(actual_autoalias) 1
set vTcl(actual_relative_placement) 0
set vTcl(mode) Relative
set vTcl(w,wm,dflt,origin) 1
}




proc vTclWindow.top32 {base} {
    global vTcl
    if {$base == ""} {
        set base .top32
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightbackground wheat \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 609x585
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Vrex Help"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.tSc33 \
        -borderwidth 2 -relief groove -background wheat -height 75 \
        -highlightbackground wheat -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.tSc33" "TScrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $top.tSc33.01 configure -background white \
        -font "-family {DejaVu Sans} -size 13" \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap word
    button $top.but34 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command close \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground black -highlightbackground wheat -highlightcolor black \
        -text Close 
    vTcl:DefineAlias "$top.but34" "Button1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TSizegrip -background $vTcl(actual_gui_bg)
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi34 \
        -cursor bottom_right_corner 
    vTcl:DefineAlias "$top.tSi34" "TSizegrip1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tSc33 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.016 -width 0 -relwidth 0.954 \
        -height 0 -relheight 0.896 -anchor nw -bordermode ignore 
    grid columnconf $top.tSc33 0 -weight 1
    grid rowconf $top.tSc33 0 -weight 1
    place $top.but34 \
        -in $top -x 0 -relx 0.4417 -y 0 -rely 0.935 -anchor nw \
        -bordermode ignore 
    place $top.tSi34 \
        -in $top -x 0 -relx 1 -y 0 -rely 1 -anchor se -bordermode inside 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
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
Window show .top32 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
