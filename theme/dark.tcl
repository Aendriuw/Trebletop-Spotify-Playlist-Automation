# Copyright (c) 2021 rdbende <rdbende@gmail.com>

# The Azure theme is a beautiful modern ttk theme inspired by Microsoft's fluent design.

package require Tk 8.6

namespace eval ttk::theme::azure-dark {
    variable version 2.0
    package provide ttk::theme::azure-dark $version

    ttk::style theme create azure-dark -parent clam -settings {
        proc load_images {imgdir} {
            variable I
            foreach file [glob -directory $imgdir *.png] {
                set img [file tail [file rootname $file]]
                set I($img) [image create photo -file $file -format png]
            }
        }

        load_images [file join [file dirname [info script]] dark]

        array set colors {
            -fg             "#ffffff"
            -bg             "#333333"
            -disabledfg     "#aaaaaa"
            -disabledbg     "#737373"
            -selectfg       "#ffffff"
            -selectbg       "#007fff"
        }

        # Layouts

        ttk::style layout Accent.TButton {
            AccentButton.button -children {
                AccentButton.padding -children {
                    AccentButton.label -side left -expand true
                } 
            }
        }

        ttk::style layout TCombobox {
            Combobox.field -sticky nswe -children {
                Combobox.padding -expand true -sticky nswe -children {
                    Combobox.textarea -sticky nswe
                }
            }
            Combobox.button -side right -sticky ns -children {
                Combobox.arrow -sticky nsew
            }
        }

        ttk::style layout TSpinbox {
            Spinbox.field -sticky nsew -children {
                Spinbox.padding -expand true -sticky nswe -children {
                    Spinbox.textarea -sticky nswe
                }
            }
            Spinbox.button -side right -sticky ns -children {
                null -side right -children {
                    Spinbox.uparrow -side top
                    Spinbox.downarrow -side bottom
                }
            }
        }

        ttk::style layout Horizontal.TSeparator {
            Horizontal.separator -sticky nswe
        }

        ttk::style layout TLabelframe {
            Labelframe.border {
                Labelframe.padding -expand 1 -children {
                    Labelframe.label -side right
                }
            }
        }

        # Elements

        # AccentButton
        ttk::style configure Accent.TButton -padding {8 4 8 4} -width -10 -anchor center

        ttk::style element create AccentButton.button image \
            [list $I(rect-accent) \
                {selected disabled} $I(rect-accent-hover) \
                disabled $I(rect-accent-hover) \
                pressed $I(rect-accent) \
                selected $I(rect-accent) \
                active $I(rect-accent-hover) \
                focus $I(rect-accent-hover) \
            ] -border 4 -sticky ewns

        # Combobox
        ttk::style map TCombobox -selectbackground [list \
            {!focus} $colors(-selectbg) \
            {readonly hover} $colors(-selectbg) \
            {readonly focus} $colors(-selectbg) \
        ]

        ttk::style map TCombobox -selectforeground [list \
            {!focus} $colors(-selectfg) \
            {readonly hover} $colors(-selectfg) \
            {readonly focus} $colors(-selectfg) \
        ]

        ttk::style element create Combobox.field \
            image [list $I(box-basic) \
                {readonly disabled} $I(rect-basic) \
                {readonly pressed} $I(rect-basic) \
                {readonly focus hover} $I(button-hover) \
                {readonly focus} $I(button-hover) \
                {readonly hover} $I(button-hover) \
                {focus hover} $I(box-accent) \
                readonly $I(rect-basic) \
                invalid $I(box-invalid) \
                disabled $I(box-basic) \
                focus $I(box-accent) \
                hover $I(box-hover) \
            ] -border 5 -padding {8}

        ttk::style element create Combobox.button \
            image [list $I(combo-button-basic) \
                 {!readonly focus} $I(combo-button-focus) \
                 {readonly focus} $I(combo-button-hover) \
                 {readonly hover} $I(combo-button-hover)
            ] -border 5 -padding {2 6 6 6}

        ttk::style element create Combobox.arrow image $I(down) \
            -width 15 -sticky e

        # Spinbox
        ttk::style element create Spinbox.field \
            image [list $I(box-basic) \
                invalid $I(box-invalid) \
                disabled $I(box-basic) \
                focus $I(box-accent) \
                hover $I(box-hover) \
            ] -border 5 -padding {8} -sticky news

        ttk::style element create Spinbox.uparrow \
            image [list $I(up) \
                disabled $I(up) \
                pressed $I(up-accent) \
                active $I(up-accent) \
            ] -border 4 -width 15 -sticky e

        ttk::style element create Spinbox.downarrow \
            image [list $I(down) \
                disabled $I(down) \
                pressed $I(down-accent) \
                active $I(down-accent) \
            ] -border 4 -width 15 -sticky e

        ttk::style element create Spinbox.button \
            image [list $I(combo-button-basic) \
                 {!readonly focus} $I(combo-button-focus) \
                 {readonly focus} $I(combo-button-hover) \
                 {readonly hover} $I(combo-button-hover)
            ] -border 5 -padding {2 6 6 6}

        # Separator
        ttk::style element create Horizontal.separator image $I(separator)

        # Labelframe
        ttk::style element create Labelframe.border image $I(card) \
            -border 5 -padding 4 -sticky news
    }
}