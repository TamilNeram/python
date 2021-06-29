// -*- C++ -*-
//
// generated by wxGlade 0.9.5 on Sun Feb  2 13:54:43 2020
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

// Note that this code file is not valid as it contains Python specific parts! It's just for testing.


#include "matplotlib_example.h"

// begin wxGlade: ::extracode
// end wxGlade



MyFrame::MyFrame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, wxDEFAULT_FRAME_STYLE)
{
    // begin wxGlade: MyFrame::MyFrame
    SetSize(wxSize(400, 300));
    panel_1 = new wxPanel(this, wxID_ANY);
    figure = self.matplotlib_figure = Figure()
    # 1x1 grid, first subplot
    self.matplotlib_axes = figure.add_subplot(111)
    matplotlib_canvas = new FigureCanvas(panel_1, wxID_ANY, figure);
    text_function = new wxTextCtrl(panel_1, wxID_ANY, wxT("sin(x)"));
    text_xmin = new wxTextCtrl(panel_1, wxID_ANY, wxT("0"));
    text_max = new wxTextCtrl(panel_1, wxID_ANY, wxT("10"));
    text_xstep = new wxTextCtrl(panel_1, wxID_ANY, wxT("0.1"));
    button_plot = new wxButton(panel_1, wxID_ANY, wxT("Plot"));
    button_clear = new wxButton(panel_1, wxID_ANY, wxT("Clear"));

    set_properties();
    do_layout();
    // end wxGlade
    // some extra code at end of MyFrame new
}


void MyFrame::set_properties()
{
    // begin wxGlade: MyFrame::set_properties
    SetTitle(wxT("matplotlib canvas example"));
    text_xmin->SetMinSize(wxSize(40, -1));
    text_max->SetMinSize(wxSize(40, -1));
    text_xstep->SetMinSize(wxSize(40, -1));
    button_plot->SetDefault();
    // end wxGlade
}


void MyFrame::do_layout()
{
    // begin wxGlade: MyFrame::do_layout
    wxBoxSizer* sizer_1 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_2 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_3 = new wxBoxSizer(wxHORIZONTAL);
    wxBoxSizer* sizer_4 = new wxBoxSizer(wxHORIZONTAL);
    sizer_2->Add(matplotlib_canvas, 1, wxALL|wxEXPAND, 3);
    wxStaticText* label_4 = new wxStaticText(panel_1, wxID_ANY, wxT("f(x) = "));
    sizer_4->Add(label_4, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5);
    sizer_4->Add(text_function, 1, 0, 0);
    sizer_2->Add(sizer_4, 0, wxALL|wxEXPAND, 5);
    wxStaticText* label_1 = new wxStaticText(panel_1, wxID_ANY, wxT("xmin"));
    sizer_3->Add(label_1, 0, wxALIGN_CENTER_VERTICAL, 0);
    sizer_3->Add(text_xmin, 0, 0, 0);
    wxStaticText* label_2 = new wxStaticText(panel_1, wxID_ANY, wxT("xmax"));
    sizer_3->Add(label_2, 0, wxALIGN_CENTER_VERTICAL, 0);
    sizer_3->Add(text_max, 0, 0, 0);
    wxStaticText* label_3 = new wxStaticText(panel_1, wxID_ANY, wxT("step"));
    sizer_3->Add(label_3, 0, wxALIGN_CENTER_VERTICAL, 0);
    sizer_3->Add(text_xstep, 0, 0, 0);
    sizer_3->Add(20, 20, 1, 0, 0);
    sizer_3->Add(button_plot, 0, 0, 0);
    sizer_3->Add(button_clear, 0, wxLEFT, 8);
    sizer_2->Add(sizer_3, 0, wxALL|wxEXPAND, 5);
    panel_1->SetSizer(sizer_2);
    sizer_1->Add(panel_1, 1, wxEXPAND, 0);
    SetSizer(sizer_1);
    Layout();
    // end wxGlade
}


BEGIN_EVENT_TABLE(MyFrame, wxFrame)
    // begin wxGlade: MyFrame::event_table
    EVT_BUTTON(wxID_ANY, MyFrame::on_button_plot)
    // end wxGlade
END_EVENT_TABLE();


void MyFrame::on_button_plot(wxCommandEvent &event)  // wxGlade: MyFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MyFrame::on_button_plot) not implemented yet"));
}

// wxGlade: add MyFrame event handlers


class MyApp: public wxApp {
public:
    bool OnInit();
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    wxInitAllImageHandlers();
    MyFrame* frame = new MyFrame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(frame);
    frame->Show();
    return true;
}


// some extra code after MyApp