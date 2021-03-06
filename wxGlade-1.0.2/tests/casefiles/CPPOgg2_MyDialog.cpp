// -*- C++ -*-
//
// generated by wxGlade "faked test version"
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#include <wx/wx.h>
#include "CPPOgg2_MyDialog.h"

// begin wxGlade: ::extracode
// end wxGlade


CPPOgg2_MyDialog::CPPOgg2_MyDialog(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxDialog(parent, id, title, pos, size, wxCAPTION|wxCLOSE_BOX|wxDEFAULT_DIALOG_STYLE|wxRESIZE_BORDER|wxSYSTEM_MENU)
{
    // begin wxGlade: CPPOgg2_MyDialog::CPPOgg2_MyDialog
    SetSize(wxSize(500, 300));
    SetTitle(_("mp3 2 ogg"));
    wxFlexGridSizer* sizer_1 = new wxFlexGridSizer(3, 1, 0, 0);
    notebook_1 = new wxNotebook(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0);
    sizer_1->Add(notebook_1, 1, wxEXPAND, 0);
    notebook_1_pane_1 = new wxPanel(notebook_1, wxID_ANY);
    notebook_1->AddPage(notebook_1_pane_1, _("Input File"));
    wxFlexGridSizer* grid_sizer_1 = new wxFlexGridSizer(1, 3, 0, 0);
    wxStaticText* label_1 = new wxStaticText(notebook_1_pane_1, wxID_ANY, _("File name:"));
    grid_sizer_1->Add(label_1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5);
    text_ctrl_1 = new wxTextCtrl(notebook_1_pane_1, wxID_ANY, wxEmptyString);
    grid_sizer_1->Add(text_ctrl_1, 1, wxALIGN_CENTER_VERTICAL|wxALL|wxEXPAND, 5);
    button_3 = new wxButton(notebook_1_pane_1, wxID_OPEN, wxEmptyString);
    grid_sizer_1->Add(button_3, 0, wxALL, 5);
    notebook_1_pane_2 = new wxPanel(notebook_1, wxID_ANY);
    notebook_1->AddPage(notebook_1_pane_2, _("Converting Options"));
    wxBoxSizer* sizer_4 = new wxBoxSizer(wxHORIZONTAL);
    const wxString radio_box_1_choices[] = {
        _("44 kbit"),
        _("128 kbit"),
    };
    radio_box_1 = new wxRadioBox(notebook_1_pane_2, wxID_ANY, _("Sampling Rate"), wxDefaultPosition, wxDefaultSize, 2, radio_box_1_choices, 0, wxRA_SPECIFY_ROWS);
    radio_box_1->SetSelection(0);
    sizer_4->Add(radio_box_1, 0, wxALL|wxEXPAND|wxSHAPED, 5);
    notebook_1_pane_3 = new wxPanel(notebook_1, wxID_ANY);
    notebook_1->AddPage(notebook_1_pane_3, _("Converting Progress"));
    wxBoxSizer* sizer_3 = new wxBoxSizer(wxHORIZONTAL);
    text_ctrl_2 = new wxTextCtrl(notebook_1_pane_3, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE);
    sizer_3->Add(text_ctrl_2, 1, wxALL|wxEXPAND, 5);
    notebook_1_pane_4 = new wxPanel(notebook_1, wxID_ANY);
    notebook_1->AddPage(notebook_1_pane_4, _("Output File"));
    wxFlexGridSizer* grid_sizer_2 = new wxFlexGridSizer(2, 3, 0, 0);
    label_2 = new wxStaticText(notebook_1_pane_4, wxID_ANY, _("File name:"));
    grid_sizer_2->Add(label_2, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5);
    text_ctrl_3 = new wxTextCtrl(notebook_1_pane_4, wxID_ANY, wxEmptyString);
    grid_sizer_2->Add(text_ctrl_3, 0, wxALL|wxEXPAND, 5);
    button_4 = new wxButton(notebook_1_pane_4, wxID_OPEN, wxEmptyString);
    grid_sizer_2->Add(button_4, 0, wxALL, 5);
    grid_sizer_2->Add(20, 20, 0, 0, 0);
    checkbox_1 = new wxCheckBox(notebook_1_pane_4, wxID_ANY, _("Overwrite existing file"));
    checkbox_1->SetToolTip(_("Overwrite an existing file"));
    checkbox_1->SetValue(1);
    grid_sizer_2->Add(checkbox_1, 0, wxALL|wxEXPAND, 5);
    grid_sizer_2->Add(20, 20, 0, 0, 0);
    static_line_1 = new wxStaticLine(this, wxID_ANY);
    sizer_1->Add(static_line_1, 0, wxALL|wxEXPAND, 5);
    wxFlexGridSizer* sizer_2 = new wxFlexGridSizer(1, 3, 0, 0);
    sizer_1->Add(sizer_2, 0, wxALIGN_RIGHT, 0);
    button_5 = new wxButton(this, wxID_CLOSE, wxEmptyString);
    sizer_2->Add(button_5, 0, wxALIGN_RIGHT|wxALL, 5);
    button_2 = new wxButton(this, wxID_CANCEL, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxBU_TOP);
    sizer_2->Add(button_2, 0, wxALIGN_RIGHT|wxALL, 5);
    button_1 = new wxButton(this, wxID_OK, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxBU_TOP);
    sizer_2->Add(button_1, 0, wxALIGN_RIGHT|wxALL, 5);
    
    grid_sizer_2->AddGrowableCol(1);
    notebook_1_pane_4->SetSizer(grid_sizer_2);
    notebook_1_pane_3->SetSizer(sizer_3);
    notebook_1_pane_2->SetSizer(sizer_4);
    grid_sizer_1->AddGrowableCol(1);
    notebook_1_pane_1->SetSizer(grid_sizer_1);
    sizer_1->AddGrowableRow(0);
    sizer_1->AddGrowableCol(0);
    SetSizer(sizer_1);
    Layout();
    Centre();
    // end wxGlade
}


void CPPOgg2_MyDialog::set_properties()
{
}


void CPPOgg2_MyDialog::do_layout()
{
}


BEGIN_EVENT_TABLE(CPPOgg2_MyDialog, wxDialog)
    // begin wxGlade: CPPOgg2_MyDialog::event_table
    EVT_BUTTON(wxID_OK, CPPOgg2_MyDialog::startConverting)
    // end wxGlade
END_EVENT_TABLE();


void CPPOgg2_MyDialog::startConverting(wxCommandEvent &event)
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (CPPOgg2_MyDialog::startConverting) not implemented yet"));
}


// wxGlade: add CPPOgg2_MyDialog event handlers

