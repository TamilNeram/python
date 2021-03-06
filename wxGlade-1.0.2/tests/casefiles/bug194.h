// -*- C++ -*-
//
// generated by wxGlade
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#ifndef BUG194_H
#define BUG194_H

#include <wx/wx.h>
#include <wx/image.h>
#include <wx/intl.h>

#ifndef APP_CATALOG
#define APP_CATALOG "app"  // replace with the appropriate catalog name
#endif


// begin wxGlade: ::dependencies
// end wxGlade

// begin wxGlade: ::extracode
// end wxGlade


class Frame194: public wxFrame {
public:
    // begin wxGlade: Frame194::ids
    // end wxGlade

    Frame194(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos=wxDefaultPosition, const wxSize& size=wxDefaultSize, long style=wxDEFAULT_FRAME_STYLE);

private:

protected:
    // begin wxGlade: Frame194::attributes
    wxListBox* list_box_single;
    wxListBox* list_box_multiple;
    wxListBox* list_box_extended;
    wxCheckListBox* check_list_box_single;
    wxCheckListBox* check_list_box_multiple;
    wxCheckListBox* check_list_box_extended;
    // end wxGlade
}; // wxGlade: end class


#endif // BUG194_H
