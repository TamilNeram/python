#!/usr/bin/perl -w -- 
#
# generated by wxGlade "faked test version"
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

package MyDialog1;

use Wx qw[:everything];
use base qw(Wx::Dialog);
use strict;

use Wx::Locale gettext => '_T';
sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyDialog1::new
    $style = wxDEFAULT_DIALOG_STYLE
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->{hyperlink_1} = Wx::HyperlinkCtrl->new($self, wxID_ANY, _T("Visit wxGlade home page"), _T("http://wxglade.sf.net"));

    $self->__set_properties();
    $self->__do_layout();

    # end wxGlade
    return $self;

}


sub __set_properties {
    my $self = shift;
    # begin wxGlade: MyDialog1::__set_properties
    $self->SetTitle(_T("dialog_2"));
    # end wxGlade
}

sub __do_layout {
    my $self = shift;
    # begin wxGlade: MyDialog1::__do_layout
    $self->{sizer_2} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_2}->Add($self->{hyperlink_1}, 1, wxALL|wxEXPAND, 5);
    $self->SetSizer($self->{sizer_2});
    $self->{sizer_2}->Fit($self);
    $self->Layout();
    # end wxGlade
}

# end of class MyDialog1

1;

package MyDialog;

use Wx qw[:everything];
use base qw(Wx::Dialog);
use strict;

use Wx::Locale gettext => '_T';
sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyDialog::new
    $style = wxDEFAULT_DIALOG_STYLE 
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->{text_ctrl_1} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE);
    $self->{static_line_1} = Wx::StaticLine->new($self, wxID_ANY);
    $self->{button_2} = Wx::Button->new($self, wxID_OK, "");
    $self->{button_1} = Wx::Button->new($self, wxID_CANCEL, "");

    $self->__set_properties();
    $self->__do_layout();

    # end wxGlade
    return $self;

}


sub __set_properties {
    my $self = shift;
    # begin wxGlade: MyDialog::__set_properties
    $self->SetTitle(_T("dialog_1"));
    $self->{button_1}->SetDefault();
    # end wxGlade
}

sub __do_layout {
    my $self = shift;
    # begin wxGlade: MyDialog::__do_layout
    $self->{grid_sizer_1} = Wx::FlexGridSizer->new(3, 1, 0, 0);
    $self->{sizer_1} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{grid_sizer_1}->Add($self->{text_ctrl_1}, 1, wxALL|wxEXPAND, 5);
    $self->{grid_sizer_1}->Add($self->{static_line_1}, 0, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{button_2}, 0, wxALL, 5);
    $self->{sizer_1}->Add($self->{button_1}, 0, wxALL, 5);
    $self->{grid_sizer_1}->Add($self->{sizer_1}, 1, wxEXPAND, 0);
    $self->SetSizer($self->{grid_sizer_1});
    $self->{grid_sizer_1}->Fit($self);
    $self->{grid_sizer_1}->AddGrowableRow(0);
    $self->Layout();
    # end wxGlade
}

# end of class MyDialog

1;

package MyApp;

use base qw(Wx::App);
use strict;

sub OnInit {
    my( $self ) = shift;

    Wx::InitAllImageHandlers();

    my $dialog_1 = MyDialog->new();

    $self->SetTopWindow($dialog_1);
    $dialog_1->Show(1);

    return 1;
}
# end of class MyApp

package main;

unless(caller){
    my $local = Wx::Locale->new("English", "en", "en"); # replace with ??
    $local->AddCatalog("app"); # replace with the appropriate catalog name

    my $app = MyApp->new();
    $app->MainLoop();
}
