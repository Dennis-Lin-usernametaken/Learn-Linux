_man = '''
        MAN(1)                                                                                                    Manual pager utils                                                                                                   MAN(1)

NAME
       man - an interface to the system reference manuals

SYNOPSIS
       man [man options] [[section] page ...] ...
       man -k [apropos options] regexp ...
       man -K [man options] [section] term ...
       man -f [whatis options] page ...
       man -l [man options] file ...
       man -w|-W [man options] page ...

DESCRIPTION
       man  is  the system's manual pager.  Each page argument given to man is normally the name of a program, utility or function.  The manual page associated with each of these arguments is then found and displayed.  A section,
       if provided, will direct man to look only in that section of the manual.  The default action is to search in all of the available sections following a pre-defined order (see DEFAULTS), and  to  show  only  the  first  page
       found, even if page exists in several sections.

       The table below shows the section numbers of the manual followed by the types of pages they contain.

       1   Executable programs or shell commands
       2   System calls (functions provided by the kernel)
       3   Library calls (functions within program libraries)
       4   Special files (usually found in /dev)
       5   File formats and conventions, e.g. /etc/passwd
       6   Games
       7   Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7)
       8   System administration commands (usually only for root)
       9   Kernel routines [Non standard]

       A manual page consists of several sections.

       Conventional section names include NAME, SYNOPSIS, CONFIGURATION, DESCRIPTION, OPTIONS, EXIT STATUS, RETURN VALUE, ERRORS, ENVIRONMENT, FILES, VERSIONS, CONFORMING TO, NOTES, BUGS, EXAMPLE, AUTHORS, and SEE ALSO.

       The following conventions apply to the SYNOPSIS section and can be used as a guide in other sections.

       bold text          type exactly as shown.
       italic text        replace with appropriate argument.
       [-abc]             any or all arguments within [ ] are optional.
       -a|-b              options delimited by | cannot be used together.
       argument ...       argument is repeatable.
       [expression] ...   entire expression within [ ] is repeatable.

       Exact rendering may vary depending on the output device.  For instance, man will usually not be able to render italics when running in a terminal, and will typically use underlined or coloured text instead.

       The  command  or  function illustration is a pattern that should match all possible invocations.  In some cases it is advisable to illustrate several exclusive invocations as is shown in the SYNOPSIS section of this manual
       page.

EXAMPLES
       man ls
           Display the manual page for the item (program) ls.

       man man.7
           Display the manual page for macro package man from section 7.  (This is an alternative spelling of "man 7 man".)

       man 'man(7)'
           Display the manual page for macro package man from section 7.  (This is another alternative spelling of "man 7 man".  It may be more convenient when copying and pasting cross-references to manual pages.  Note that  the
           parentheses must normally be quoted to protect them from the shell.)

       man -a intro
           Display, in succession, all of the available intro manual pages contained within the manual.  It is possible to quit between successive displays or skip any of them.

       man -t bash | lpr -Pps
           Format  the manual page for bash into the default troff or groff format and pipe it to the printer named ps.  The default output for groff is usually PostScript.  man --help should advise as to which processor is bound
           to the -t option.

       man -l -Tdvi ./foo.1x.gz > ./foo.1x.dvi
           This command will decompress and format the nroff source manual page ./foo.1x.gz into a device independent (dvi) file.  The redirection is necessary as the -T flag causes output to be directed to stdout with no  pager.
           The output could be viewed with a program such as xdvi or further processed into PostScript using a program such as dvips.

       man -k printf
           Search the short descriptions and manual page names for the keyword printf as regular expression.  Print out any matches.  Equivalent to apropos printf.

       man -f smail
           Lookup the manual pages referenced by smail and print out the short descriptions of any found.  Equivalent to whatis smail.

OVERVIEW
       Many options are available to man in order to give as much flexibility as possible to the user.  Changes can be made to the search path, section order, output processor, and other behaviours and operations detailed below.

       If  set,  various  environment  variables are interrogated to determine the operation of man.  It is possible to set the "catch-all" variable $MANOPT to any string in command line format, with the exception that any spaces
       used as part of an option's argument must be escaped (preceded by a backslash).  man will parse $MANOPT prior to parsing its own command line.  Those options requiring an argument will be overridden  by  the  same  options
       found  on  the  command line.  To reset all of the options set in $MANOPT, -D can be specified as the initial command line option.  This will allow man to "forget" about the options specified in $MANOPT, although they must
       still have been valid.

       Manual pages are normally stored in nroff(1) format under a directory such as /usr/share/man.  In some installations, there may also be preformatted cat pages to improve performance.  See manpath(5) for  details  of  where
       these files are stored.

       This  package supports manual pages in multiple languages, controlled by your locale.  If your system did not set this up for you automatically, then you may need to set $LC_MESSAGES, $LANG, or another system-dependent en‐
       vironment variable to indicate your preferred locale, usually specified in the POSIX format:

       <language>[_<territory>[.<character-set>[,<version>]]]

       If the desired page is available in your locale, it will be displayed in lieu of the standard (usually American English) page.

       If you find that the translations supplied with this package are not available in your native language and you would like to supply them, please contact the maintainer who will be coordinating such activity.

       Individual manual pages are normally written and maintained by the maintainers of the program, function, or other topic that they document, and are not included with this package.  If you find that a manual page is missing
       or inadequate, please report that to the maintainers of the package in question.

       For information regarding other features and extensions available with this manual pager, please read the documents supplied with the package.

DEFAULTS
       The order of sections to search may be overridden by the environment variable $MANSECT or by the SECTION directive in /etc/manpath.config.  By default it is as follows:

              1 n l 8 3 2 3posix 3pm 3perl 3am 5 4 9 6 7

       The formatted manual page is displayed using a pager.  This can be specified in a number of ways, or else will fall back to a default (see option -P for details).

       The  filters are deciphered by a number of means.  Firstly, the command line option -p or the environment variable $MANROFFSEQ is interrogated.  If -p was not used and the environment variable was not set, the initial line
       of the nroff file is parsed for a preprocessor string.  To contain a valid preprocessor string, the first line must resemble

       '\" <string>

       where string can be any combination of letters described by option -p below.

       If none of the above methods provide any filter information, a default set is used.

       A formatting pipeline is formed from the filters and the primary formatter (nroff or [tg]roff with -t) and executed.  Alternatively, if an executable program mandb_nfmt (or mandb_tfmt with -t) exists in the man tree  root,
       it is executed instead.  It gets passed the manual source file, the preprocessor string, and optionally the device specified with -T or -E as arguments.

OPTIONS
       Non-argument options that are duplicated either on the command line, in $MANOPT, or both, are not harmful.  For options that require an argument, each duplication will override the previous argument value.

   General options
       -C file, --config-file=file
              Use this user configuration file rather than the default of ~/.manpath.

       -d, --debug
              Print debugging information.

       -D, --default
              This  option  is  normally issued as the very first option and resets man's behaviour to its default.  Its use is to reset those options that may have been set in $MANOPT.  Any options that follow -D will have their
              usual effect.

       --warnings[=warnings]
              Enable warnings from groff.  This may be used to perform sanity checks on the source text of manual pages.  warnings is a comma-separated list of warning names; if it is not supplied, the default is "mac".  See  the
              “Warnings” node in info groff for a list of available warning names.

   Main modes of operation
       -f, --whatis
              Equivalent to whatis.  Display a short description from the manual page, if available.  See whatis(1) for details.

       -k, --apropos
              Equivalent to apropos.  Search the short manual page descriptions for keywords and display any matches.  See apropos(1) for details.

       -K, --global-apropos
              Search for text in all manual pages.  This is a brute-force search, and is likely to take some time; if you can, you should specify a section to reduce the number of pages that need to be searched.  Search terms may
              be simple strings (the default), or regular expressions if the --regex option is used.

              Note that this searches the sources of the manual pages, not the rendered text, and so may include false positives due to things like comments in source files.  Searching the rendered text would be much slower.

       -l, --local-file
              Activate "local" mode.  Format and display local manual files instead of searching through the system's manual collection.  Each manual page argument will be interpreted as an nroff source file in the  correct  for‐
              mat.   No cat file is produced.  If '-' is listed as one of the arguments, input will be taken from stdin.  When this option is not used, and man fails to find the page required, before displaying the error message,
              it attempts to act as if this option was supplied, using the name as a filename and looking for an exact match.

       -w, --where, --path, --location
              Don't actually display the manual page, but do print the location of the source nroff file that would be formatted.  If the -a option is also used, then print the locations of all source files that match the  search
              criteria.

   Main modes of operation
       -f, --whatis
              Equivalent to whatis.  Display a short description from the manual page, if available.  See whatis(1) for details.

       -k, --apropos
              Equivalent to apropos.  Search the short manual page descriptions for keywords and display any matches.  See apropos(1) for details.

       -K, --global-apropos
              Search for text in all manual pages.  This is a brute-force search, and is likely to take some time; if you can, you should specify a section to reduce the number of pages that need to be searched.  Search terms may
              be simple strings (the default), or regular expressions if the --regex option is used.

              Note that this searches the sources of the manual pages, not the rendered text, and so may include false positives due to things like comments in source files.  Searching the rendered text would be much slower.

       -l, --local-file
              Activate "local" mode.  Format and display local manual files instead of searching through the system's manual collection.  Each manual page argument will be interpreted as an nroff source file in the  correct  for‐
              mat.   No cat file is produced.  If '-' is listed as one of the arguments, input will be taken from stdin.  When this option is not used, and man fails to find the page required, before displaying the error message,
              it attempts to act as if this option was supplied, using the name as a filename and looking for an exact match.

       -w, --where, --path, --location
              Don't actually display the manual page, but do print the location of the source nroff file that would be formatted.  If the -a option is also used, then print the locations of all source files that match the  search
              criteria.

       -W, --where-cat, --location-cat
              Don't  actually  display  the  manual page, but do print the location of the preformatted cat file that would be displayed.  If the -a option is also used, then print the locations of all preformatted cat files that
              match the search criteria.

              If -w and -W are both used, then print both source file and cat file separated by a space.  If all of -w, -W, and -a are used, then do this for each possible match.

       -c, --catman
              This option is not for general use and should only be used by the catman program.

       -R encoding, --recode=encoding
              Instead of formatting the manual page in the usual way, output its source converted to the specified encoding.  If you already know the encoding of the source file, you can also use  manconv(1)  directly.   However,
              this  option allows you to convert several manual pages to a single encoding without having to explicitly state the encoding of each, provided that they were already installed in a structure similar to a manual page
              hierarchy.

              Consider using man-recode(1) instead for converting multiple manual pages, since it has an interface designed for bulk conversion and so can be much faster.

   Finding manual pages
       -L locale, --locale=locale
              man will normally determine your current locale by a call to the C function setlocale(3) which interrogates various environment variables, possibly including $LC_MESSAGES and $LANG.  To temporarily override the  de‐
              termined  value, use this option to supply a locale string directly to man.  Note that it will not take effect until the search for pages actually begins.  Output such as the help message will always be displayed in
              the initially determined locale.

       -m system[,...], --systems=system[,...]
              If this system has access to other operating system's manual pages, they can be accessed using this option.  To search for a manual page from NewOS's manual page collection, use the option -m NewOS.

              The system specified can be a combination of comma delimited operating system names.  To include a search of the native operating system's manual pages, include the system name man in the argument string.  This  op‐
              tion will override the $SYSTEM environment variable.

       -M path, --manpath=path
              Specify an alternate manpath to use.  By default, man uses manpath derived code to determine the path to search.  This option overrides the $MANPATH environment variable and causes option -m to be ignored.

              A  path specified as a manpath must be the root of a manual page hierarchy structured into sections as described in the man-db manual (under "The manual page system").  To view manual pages outside such hierarchies,
              see the -l option.

       -S list, -s list, --sections=list
              The given list is a colon- or comma-separated list of sections, used to determine which manual sections to search and in what order.  This option overrides the $MANSECT environment variable.  (The -s spelling is for
              compatibility with System V.)

       -e sub-extension, --extension=sub-extension
              Some  systems  incorporate  large packages of manual pages, such as those that accompany the Tcl package, into the main manual page hierarchy.  To get around the problem of having two manual pages with the same name
              such as exit(3), the Tcl pages were usually all assigned to section l.  As this is unfortunate, it is now possible to put the pages in the correct section, and to assign a specific "extension" to them, in this case,
              exit(3tcl).   Under  normal operation, man will display exit(3) in preference to exit(3tcl).  To negotiate this situation and to avoid having to know which section the page you require resides in, it is now possible
              to give man a sub-extension string indicating which package the page must belong to.  Using the above example, supplying the option -e tcl to man will restrict the search to pages having an extension of *tcl.

       -i, --ignore-case
              Ignore case when searching for manual pages.  This is the default.

       -I, --match-case
              Search for manual pages case-sensitively.

       --regex
              Show all pages with any part of either their names or their descriptions matching each page argument as a regular expression, as with apropos(1).  Since there is usually no reasonable way to pick a "best" page  when
              searching for a regular expression, this option implies -a.

       --wildcard
              Show  all  pages with any part of either their names or their descriptions matching each page argument using shell-style wildcards, as with apropos(1) --wildcard.  The page argument must match the entire name or de‐
              scription, or match on word boundaries in the description.  Since there is usually no reasonable way to pick a "best" page when searching for a wildcard, this option implies -a.

       --names-only
              If the --regex or --wildcard option is used, match only page names, not page descriptions, as with whatis(1).  Otherwise, no effect.

       -a, --all
              By default, man will exit after displaying the most suitable manual page it finds.  Using this option forces man to display all the manual pages with names that match the search criteria.

       -u, --update
              This option causes man to update its database caches of installed manual pages.  This is only needed in rare situations, and it is normally better to run mandb(8) instead.

       --no-subpages
              By default, man will try to interpret pairs of manual page names given on the command line as equivalent to a single manual page name containing a hyphen or an underscore.  This supports the common pattern  of  pro‐
              grams that implement a number of subcommands, allowing them to provide manual pages for each that can be accessed using similar syntax as would be used to invoke the subcommands themselves.  For example:

                $ man -aw git diff
                /usr/share/man/man1/git-diff.1.gz

              To disable this behaviour, use the --no-subpages option.

                $ man -aw --no-subpages git diff
                /usr/share/man/man1/git.1.gz
                /usr/share/man/man3/Git.3pm.gz
                /usr/share/man/man1/diff.1.gz

   Controlling formatted output
       -P pager, --pager=pager
              Specify  which output pager to use.  By default, man uses pager, falling back to cat if pager is not found or is not executable.  This option overrides the $MANPAGER environment variable, which in turn overrides the
              $PAGER environment variable.  It is not used in conjunction with -f or -k.

              The value may be a simple command name or a command with arguments, and may use shell quoting (backslashes, single quotes, or double quotes).  It may not use pipes to connect multiple commands; if you need that, use
              a wrapper script, which may take the file to display either as an argument or on standard input.

       -r prompt, --prompt=prompt
              If a recent version of less is used as the pager, man will attempt to set its prompt and some sensible options.  The default prompt looks like

               Manual page name(sec) line x

              where name denotes the manual page name, sec denotes the section it was found under and x the current line number.  This is achieved by using the $LESS environment variable.

              Supplying  -r  with  a  string  will override this default.  The string may contain the text $MAN_PN which will be expanded to the name of the current manual page and its section name surrounded by "(" and ")".  The
              string used to produce the default could be expressed as

              \ Manual\ page\ \$MAN_PN\ ?ltline\ %lt?L/%L.:
              byte\ %bB?s/%s..?\ (END):?pB\ %pB\\%..
              (press h for help or q to quit)

              It is broken into three lines here for the sake of readability only.  For its meaning see the less(1) manual page.  The prompt string is first evaluated by the shell.  All double quotes, back-quotes and  backslashes
              in the prompt must be escaped by a preceding backslash.  The prompt string may end in an escaped $ which may be followed by further options for less.  By default man sets the -ix8 options.

              The $MANLESS environment variable described below may be used to set a default prompt string if none is supplied on the command line.

       -7, --ascii
              When viewing a pure ascii(7) manual page on a 7 bit terminal or terminal emulator, some characters may not display correctly when using the latin1(7) device description with GNU nroff.  This option allows pure ascii
              manual pages to be displayed in ascii with the latin1 device.  It will not translate any latin1 text.  The following table shows the translations performed: some parts of it may only be displayed properly when using
              GNU nroff's latin1(7) device.

              Description           Octal   latin1   ascii
              ─────────────────────────────────────────────
              continuation hyphen    255      ‐        -
              bullet (middle dot)    267      •        o
              acute accent           264      ´        '
              multiplication sign    327      ×        x

              If  the  latin1 column displays correctly, your terminal may be set up for latin1 characters and this option is not necessary.  If the latin1 and ascii columns are identical, you are reading this page using this op‐
              tion or man did not format this page using the latin1 device description.  If the latin1 column is missing or corrupt, you may need to view manual pages with this option.

              This option is ignored when using options -t, -H, -T, or -Z and may be useless for nroff other than GNU's.

       -E encoding, --encoding=encoding
              Generate output for a character encoding other than the default.  For backward compatibility, encoding may be an nroff device such as ascii, latin1, or utf8 as well as a true character encoding such as UTF-8.

       --no-hyphenation, --nh
              Normally, nroff will automatically hyphenate text at line breaks even in words that do not contain hyphens, if it is necessary to do so to lay out words on a line without excessive spacing.  This option disables au‐
              tomatic hyphenation, so words will only be hyphenated if they already contain hyphens.

              If  you  are  writing  a manual page and simply want to prevent nroff from hyphenating a word at an inappropriate point, do not use this option, but consult the nroff documentation instead; for instance, you can put
              "\%" inside a word to indicate that it may be hyphenated at that point, or put "\%" at the start of a word to prevent it from being hyphenated.

       --no-justification, --nj
              Normally, nroff will automatically justify text to both margins.  This option disables full justification, leaving justified only to the left margin, sometimes called "ragged-right" text.

              If you are writing a manual page and simply want to prevent nroff from justifying certain paragraphs, do not use this option, but consult the nroff documentation instead; for instance, you can use the ".na",  ".nf",
              ".fi", and ".ad" requests to temporarily disable adjusting and filling.

       -p string, --preprocessor=string
              Specify the sequence of preprocessors to run before nroff or troff/groff.  Not all installations will have a full set of preprocessors.  Some of the preprocessors and the letters used to designate them are: eqn (e),
              grap (g), pic (p), tbl (t), vgrind (v), refer (r).  This option overrides the $MANROFFSEQ environment variable.  zsoelim is always run as the very first preprocessor.

       -t, --troff
              Use groff -mandoc to format the manual page to stdout.  This option is not required in conjunction with -H, -T, or -Z.

       -T[device], --troff-device[=device]
              This option is used to change groff (or possibly troff's) output to be suitable for a device other than the default.  It implies -t.  Examples (provided with Groff-1.17) include dvi, latin1, ps, utf8, X75 and X100.

       -H[browser], --html[=browser]
              This option will cause groff to produce HTML output, and will display that output in a web browser.  The choice of browser is determined by the optional browser argument if one is provided, by the $BROWSER  environ‐
              ment variable, or by a compile-time default if that is unset (usually lynx).  This option implies -t, and will only work with GNU troff.

       -X[dpi], --gxditview[=dpi]
              This  option  displays  the  output of groff in a graphical window using the gxditview program.  The dpi (dots per inch) may be 75, 75-12, 100, or 100-12, defaulting to 75; the -12 variants use a 12-point base font.
              This option implies -T with the X75, X75-12, X100, or X100-12 device respectively.

       -Z, --ditroff
              groff will run troff and then use an appropriate post-processor to produce output suitable for the chosen device.  If groff -mandoc is groff, this option is passed to groff and will suppress the use of  a  post-pro‐
              cessor.  It implies -t.

   Getting help
       -?, --help
              Print a help message and exit.

       --usage
              Print a short usage message and exit.

       -V, --version
              Display version information.

EXIT STATUS
       0      Successful program execution.

       1      Usage, syntax or configuration file error.

       2      Operational error.

       3      A child process returned a non-zero exit status.

       16     At least one of the pages/files/keywords didn't exist or wasn't matched.

ENVIRONMENT
       MANPATH
              If $MANPATH is set, its value is used as the path to search for manual pages.

       MANROFFOPT
              Every time man invokes the formatter (nroff, troff, or groff), it adds the contents of $MANROFFOPT to the formatter's command line.

       MANROFFSEQ
              If $MANROFFSEQ is set, its value is used to determine the set of preprocessors to pass each manual page through.  The default preprocessor list is system dependent.

       MANSECT
              If $MANSECT is set, its value is a colon-delimited list of sections and it is used to determine which manual sections to search and in what order.  The default is "1 n l 8 3 2 3posix 3pm 3perl 3am 5 4 9 6 7", unless
              overridden by the SECTION directive in /etc/manpath.config.

       MANPAGER, PAGER
              If $MANPAGER or $PAGER is set ($MANPAGER is used in preference), its value is used as the name of the program used to display the manual page.  By default, pager is used, falling back to cat if pager is not found or
              is not executable.

              The value may be a simple command name or a command with arguments, and may use shell quoting (backslashes, single quotes, or double quotes).  It may not use pipes to connect multiple commands; if you need that, use
              a wrapper script, which may take the file to display either as an argument or on standard input.

       MANLESS
              If $MANLESS is set, its value will be used as the default prompt string for the less pager, as if it had been passed using the -r option (so any occurrences of the text $MAN_PN will be expanded  in  the  same  way).
              For example, if you want to set the prompt string unconditionally to “my prompt string”, set $MANLESS to ‘-Psmy prompt string’.  Using the -r option overrides this environment variable.

       BROWSER
              If  $BROWSER  is  set,  its value is a colon-delimited list of commands, each of which in turn is used to try to start a web browser for man --html.  In each command, %s is replaced by a filename containing the HTML
              output from groff, %% is replaced by a single percent sign (%), and %c is replaced by a colon (:).

       SYSTEM If $SYSTEM is set, it will have the same effect as if it had been specified as the argument to the -m option.

       MANOPT If $MANOPT is set, it will be parsed prior to man's command line and is expected to be in a similar format.  As all of the other man specific environment variables can be expressed as command line options,  and  are
              thus candidates for being included in $MANOPT it is expected that they will become obsolete.  N.B.  All spaces that should be interpreted as part of an option's argument must be escaped.

       MANWIDTH
              If  $MANWIDTH  is set, its value is used as the line length for which manual pages should be formatted.  If it is not set, manual pages will be formatted with a line length appropriate to the current terminal (using
              the value of $COLUMNS, and ioctl(2) if available, or falling back to 80 characters if neither is available).  Cat pages will only be saved when the default formatting can be used, that  is  when  the  terminal  line
              length is between 66 and 80 characters.

       MAN_KEEP_FORMATTING
              Normally, when output is not being directed to a terminal (such as to a file or a pipe), formatting characters are discarded to make it easier to read the result without special tools.  However, if $MAN_KEEP_FORMAT‐
              TING is set to any non-empty value, these formatting characters are retained.  This may be useful for wrappers around man that can interpret formatting characters.

       MAN_KEEP_STDERR
              Normally, when output is being directed to a terminal (usually to a pager), any error output from the command used to produce formatted versions of manual pages is discarded to avoid  interfering  with  the  pager's
              display.   Programs  such  as groff often produce relatively minor error messages about typographical problems such as poor alignment, which are unsightly and generally confusing when displayed along with the manual
              page.  However, some users want to see them anyway, so, if $MAN_KEEP_STDERR is set to any non-empty value, error output will be displayed as usual.

       LANG, LC_MESSAGES
              Depending on system and implementation, either or both of $LANG and $LC_MESSAGES will be interrogated for the current message locale.  man will display its messages in that locale (if available).   See  setlocale(3)
              for precise details.

FILES
       /etc/manpath.config
              man-db configuration file.

       /usr/share/man
              A global manual page hierarchy.

SEE ALSO
       apropos(1), groff(1), less(1), manpath(1), nroff(1), troff(1), whatis(1), zsoelim(1), manpath(5), man(7), catman(8), mandb(8)

       Documentation for some packages may be available in other formats, such as info(1) or HTML.

HISTORY
       1990, 1991 – Originally written by John W. Eaton (jwe@che.utexas.edu).

       Dec 23 1992: Rik Faith (faith@cs.unc.edu) applied bug fixes supplied by Willem Kasdorp (wkasdo@nikhefk.nikef.nl).

       30th April 1994 – 23rd February 2000: Wilf. (G.Wilford@ee.surrey.ac.uk) has been developing and maintaining this package with the help of a few dedicated people.

       30th October 1996 – 30th March 2001: Fabrizio Polacco <fpolacco@debian.org> maintained and enhanced this package for the Debian project, with the help of all the community.

       31st March 2001 – present day: Colin Watson <cjwatson@debian.org> is now developing and maintaining man-db.

BUGS
       https://savannah.nongnu.org/bugs/?group=man-db

2.9.3                                                                                                         2020-06-22                                                                                                       MAN(1)
        
        '''








_ls = '''
        LS(1)                                                                                                       User Commands                                                                                                       LS(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
       ls - list directory contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
SYNOPSIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
       ls [OPTION]... [FILE]...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
       List information about the FILEs (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       Mandatory arguments to long options are mandatory for short options too.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -a, --all                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              do not ignore entries starting with .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -A, --almost-all                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
              do not list implied . and ..                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --author                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
              with -l, print the author of each file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -b, --escape                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
              print C-style escapes for nongraphic characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --block-size=SIZE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
              with -l, scale sizes by SIZE when printing them; e.g., '--block-size=M'; see SIZE format below                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -B, --ignore-backups                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
              do not list implied entries ending with ~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -c     with -lt: sort by, and show, ctime (time of last modification of file status information); with -l: show ctime and sort by name; otherwise: sort by ctime, newest first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -C     list entries by columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --color[=WHEN]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              colorize the output; WHEN can be 'always' (default if omitted), 'auto', or 'never'; more info below                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -d, --directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
              list directories themselves, not their contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -D, --dired                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
              generate output designed for Emacs' dired mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -f     do not sort, enable -aU, disable -ls --color                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -F, --classify                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              append indicator (one of */=>@|) to entries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --file-type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
              likewise, except do not append '*'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --format=WORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
              across -x, commas -m, horizontal -x, long -l, single-column -1, verbose -l, vertical -C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --full-time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
              like -l --time-style=full-iso                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -g     like -l, but do not list owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --group-directories-first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              group directories before files;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              can be augmented with a --sort option, but any use of --sort=none (-U) disables grouping                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -G, --no-group                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              in a long listing, don't print group names                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -h, --human-readable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
              with -l and -s, print sizes like 1K 234M 2G etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --si   likewise, but use powers of 1000 not 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -H, --dereference-command-line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              follow symbolic links listed on the command line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --dereference-command-line-symlink-to-dir                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              follow each command line symbolic link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              that points to a directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --hide=PATTERN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              do not list implied entries matching shell PATTERN (overridden by -a or -A)

       --hyperlink[=WHEN]
              hyperlink file names; WHEN can be 'always' (default if omitted), 'auto', or 'never'

       --indicator-style=WORD
              append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)

       -i, --inode
              print the index number of each file

       -I, --ignore=PATTERN
              do not list implied entries matching shell PATTERN

       -k, --kibibytes
              default to 1024-byte blocks for disk usage; used only with -s and per directory totals

       -l     use a long listing format

       -L, --dereference
              when showing file information for a symbolic link, show information for the file the link references rather than for the link itself

       -m     fill width with a comma separated list of entries

       -n, --numeric-uid-gid
              like -l, but list numeric user and group IDs

       -N, --literal
              print entry names without quoting

       -o     like -l, but do not list group information

       -p, --indicator-style=slash
              append / indicator to directories

       -q, --hide-control-chars
              print ? instead of nongraphic characters

       --show-control-chars
              show nongraphic characters as-is (the default, unless program is 'ls' and output is a terminal)

       -Q, --quote-name
              enclose entry names in double quotes

       --quoting-style=WORD
              use quoting style WORD for entry names: literal, locale, shell, shell-always, shell-escape, shell-escape-always, c, escape (overrides QUOTING_STYLE environment variable)

       -r, --reverse
              reverse order while sorting

       -R, --recursive
              list subdirectories recursively

       -s, --size
              print the allocated size of each file, in blocks

       -S     sort by file size, largest first

       --sort=WORD
              sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)

       --time=WORD
              with -l, show time as WORD instead of default modification time: atime or access or use (-u); ctime or status (-c); also use specified time as sort key if --sort=time (newest first)

       --time-style=TIME_STYLE
              time/date format with -l; see TIME_STYLE below

       -t     sort by modification time, newest first

       -T, --tabsize=COLS
              assume tab stops at each COLS instead of 8

       -u     with -lt: sort by, and show, access time; with -l: show access time and sort by name; otherwise: sort by access time, newest first

       -U     do not sort; list entries in directory order

       -v     natural sort of (version) numbers within text

       -w, --width=COLS
              set output width to COLS.  0 means no limit

       -x     list entries by lines instead of by columns

       -X     sort alphabetically by entry extension

       -Z, --context
              print any security context of each file

       -1     list one file per line.  Avoid '\n' with -q or -b

       --help display this help and exit

       --version
              output version information and exit

       The SIZE argument is an integer and optional unit (example: 10K is 10*1024).  Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

       The  TIME_STYLE  argument  can  be  full-iso, long-iso, iso, locale, or +FORMAT.  FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FORMAT2 to recent
       files.  TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.  Also the TIME_STYLE environment variable sets the default style to use.

       Using color to distinguish file types is disabled both by default and with --color=never.  With --color=auto, ls emits color codes only when standard output is connected to a terminal.  The LS_COLORS  environment  variable
       can change the settings.  Use the dircolors command to set it.

   Exit status:
       0      if OK,

       1      if minor problems (e.g., cannot access subdirectory),

       2      if serious trouble (e.g., cannot access command-line argument).

AUTHOR
       Written by Richard M. Stallman and David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report ls translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <https://www.gnu.org/software/coreutils/ls>
       or available locally via: info '(coreutils) ls invocation'

GNU coreutils 8.30                                                                                           August 2019                                                                                                        LS(1)
        '''

_cat = '''
CAT(1)                                                                                                                       User Commands                                                                                                                      CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s) to standard output.

       With no FILE, or when FILE is -, read standard input.

       -A, --show-all
              equivalent to -vET

       -b, --number-nonblank
              number nonempty output lines, overrides -n

       -e     equivalent to -vE

       -E, --show-ends
              display $ at end of each line

       -n, --number
              number all output lines

       -s, --squeeze-blank
              suppress repeated empty output lines

       -t     equivalent to -vT

       -T, --show-tabs
              display TAB characters as ^I

       -u     (ignored)

       -v, --show-nonprinting
              use ^ and M- notation, except for LFD and TAB

       --help display this help and exit

       --version
              output version information and exit

EXAMPLES
       cat f - g
              Output f's contents, then standard input, then g's contents.

       cat    Copy standard input to standard output.

AUTHOR
       Written by Torbjorn Granlund and Richard M. Stallman.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report cat translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       tac(1)

       Full documentation at: <https://www.gnu.org/software/coreutils/cat>
       or available locally via: info '(coreutils) cat invocation'

GNU coreutils 8.30                                                                                                            August 2019              

'''

_clear = '''
clear(1)                                                                                                                                      General Commands Manual                                                                                                                                     clear(1)

NAME
       clear - clear the terminal screen

SYNOPSIS
       clear [-Ttype] [-V] [-x]

DESCRIPTION
       clear clears your screen if this is possible, including its scrollback buffer (if the extended “E3” capability is defined).  clear looks in the environment for the terminal type given by the environment variable TERM, and then in the terminfo database to determine how to clear the screen.

       clear writes to the standard output.  You can redirect the standard output to a file (which prevents clear from actually clearing the screen), and later cat the file to the screen, clearing it at that point.

OPTIONS
       -T type
            indicates the type of terminal.  Normally this option is unnecessary, because the default is taken from the environment variable TERM.  If -T is specified, then the shell variables LINES and COLUMNS will also be ignored.

       -V   reports the version of ncurses which was used in this program, and exits.  The options are as follows:

       -x   do not attempt to clear the terminal's scrollback buffer using the extended “E3” capability.

HISTORY
       A clear command appeared in 2.79BSD dated February 24, 1979.  Later that was provided in Unix 8th edition (1985).

       AT&T adapted a different BSD program (tset) to make a new command (tput), and used this to replace the clear command with a shell script which calls tput clear, e.g.,

           /usr/bin/tput ${1:+-T$1} clear 2> /dev/null
           exit

       In 1989, when Keith Bostic revised the BSD tput command to make it similar to the AT&T tput, he added a shell script for the clear command:

           exec tput clear

       The remainder of the script in each case is a copyright notice.

       The ncurses clear command began in 1995 by adapting the original BSD clear command (with terminfo, of course).

       The E3 extension came later:

       •   In June 1999, xterm provided an extension to the standard control sequence for clearing the screen.  Rather than clearing just the visible part of the screen using

               printf '\033[2J'

           one could clear the scrollback using

               printf '\033[3J'

           This is documented in XTerm Control Sequences as a feature originating with xterm.

       •   A few other terminal developers adopted the feature, e.g., PuTTY in 2006.

       •   In April 2011, a Red Hat developer submitted a patch to the Linux kernel, modifying its console driver to do the same thing.  The Linux change, part of the 3.0 release, did not mention xterm, although it was cited in the Red Hat bug report (#683733) which led to the change.

       •   Again, a few other terminal developers adopted the feature.  But the next relevant step was a change to the clear program in 2013 to incorporate this extension.

       •   In 2013, the E3 extension was overlooked in tput with the “clear” parameter.  That was addressed in 2016 by reorganizing tput to share its logic with clear and tset.

PORTABILITY
       Neither IEEE Std 1003.1/The Open  Group  Base  Specifications  Issue  7 (POSIX.1-2008) nor X/Open Curses Issue 7 documents tset or reset.

       The latter documents tput, which could be used to replace this utility either via a shell script or by an alias (such as a symbolic link) to run tput as clear.

SEE ALSO
       tput(1), terminfo(5)

       This describes ncurses version 6.2 (patch 20200212).

                                                                                                                                                                                                                                                                                                          clear(1)        

'''

_touch = '''
TOUCH(1)                                                                                                                                                                         User Commands                                                                                                                                                                         TOUCH(1)

NAME
       touch - change file timestamps

SYNOPSIS
       touch [OPTION]... FILE...

DESCRIPTION
       Update the access and modification times of each FILE to the current time.

       A FILE argument that does not exist is created empty, unless -c or -h is supplied.

       A FILE argument string of - is handled specially and causes touch to change the times of the file associated with standard output.

       Mandatory arguments to long options are mandatory for short options too.

       -a     change only the access time

       -c, --no-create
              do not create any files

       -d, --date=STRING
              parse STRING and use it instead of current time

       -f     (ignored)

       -h, --no-dereference
              affect each symbolic link instead of any referenced file (useful only on systems that can change the timestamps of a symlink)

       -m     change only the modification time

       -r, --reference=FILE
              use this file's times instead of current time

       -t STAMP
              use [[CC]YY]MMDDhhmm[.ss] instead of current time

       --time=WORD
              change the specified time: WORD is access, atime, or use: equivalent to -a WORD is modify or mtime: equivalent to -m

       --help display this help and exit

       --version
              output version information and exit

       Note that the -d and -t options accept different time-date formats.

DATE STRING
       The  --date=STRING  is  a mostly free format human readable date string such as "Sun, 29 Feb 2004 16:21:42 -0800" or "2004-02-29 16:21:42" or even "next Thursday".  A date string may contain items indicating calendar date, time of day, time zone, day of week, relative time, relative date, and numbers.  An empty string indicates the beginning of the day.  The
       date string format is more complex than is easily documented here but is fully described in the info documentation.

AUTHOR
       Written by Paul Rubin, Arnold Robbins, Jim Kingdon, David MacKenzie, and Randy Smith.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report touch translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <https://www.gnu.org/software/coreutils/touch>
       or available locally via: info '(coreutils) touch invocation'

GNU coreutils 8.30                                                                                                                                                                August 2019                                                                                                                                                                          TOUCH(1)

'''

_chmod = '''
CHMOD(1)                                                                                                                                                                         User Commands                                                                                                                                                                         CHMOD(1)                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
       chmod - change file mode bits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
SYNOPSIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
       chmod [OPTION]... MODE[,MODE]... FILE...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
       chmod [OPTION]... OCTAL-MODE FILE...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
       chmod [OPTION]... --reference=RFILE FILE...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
       This manual page documents the GNU version of chmod.  chmod changes the file mode bits of each given file according to mode, which can be either a symbolic representation of changes to make, or an octal number representing the bit pattern for the new mode bits.                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       The format of a symbolic mode is [ugoa...][[-+=][perms...]...], where perms is either zero or more letters from the set rwxXst, or a single letter from the set ugo.  Multiple symbolic modes can be given, separated by commas.                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       A combination of the letters ugoa controls which users' access to the file will be changed: the user who owns it (u), other users in the file's group (g), other users not in the file's group (o), or all users (a).  If none of these are given, the effect is as if (a) were given, but bits that are set in the umask are not affected.                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       The operator + causes the selected file mode bits to be added to the existing file mode bits of each file; - causes them to be removed; and = causes them to be added and causes unmentioned bits to be removed except that a directory's unmentioned set user and group ID bits are not affected.                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       The  letters rwxXst select file mode bits for the affected users: read (r), write (w), execute (or search for directories) (x), execute/search only if the file is a directory or already has execute permission for some user (X), set user or group ID on execution (s), restricted deletion flag or sticky bit (t).  Instead of one or more of these letters, you can                                                                                                                                                                                                                                                                      
       specify exactly one of the letters ugo: the permissions granted to the user who owns the file (u), the permissions granted to other users who are members of the file's group (g), and the permissions granted to users that are in neither of the two preceding categories (o).                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       A numeric mode is from one to four octal digits (0-7), derived by adding up the bits with values 4, 2, and 1.  Omitted digits are assumed to be leading zeros.  The first digit selects the set user ID (4) and set group ID (2) and restricted deletion or sticky (1) attributes.  The second digit selects permissions for the user who owns the file: read (4), write                                                                                                                                                                                                                                                                      
       (2), and execute (1); the third selects permissions for other users in the file's group, with the same values; and the fourth for other users not in the file's group, with the same values.                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       chmod  never  changes the permissions of symbolic links; the chmod system call cannot change their permissions.  This is not a problem since the permissions of symbolic links are never used.  However, for each symbolic link listed on the command line, chmod changes the permissions of the pointed-to file.  In contrast, chmod ignores symbolic links encountered                                                                                                                                                                                                                                                                      
       during recursive directory traversals.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
SETUID AND SETGID BITS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       chmod clears the set-group-ID bit of a regular file if the file's group ID does not match the user's effective group ID or one of the user's supplementary group IDs, unless the user has appropriate privileges.  Additional restrictions may cause the set-user-ID and set-group-ID bits of MODE or RFILE to be ignored.  This behavior  depends  on  the  policy  and                                                                                                                                                                                                                                                                      
       functionality of the underlying chmod system call.  When in doubt, check the underlying system behavior.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       For directories chmod preserves set-user-ID and set-group-ID bits unless you explicitly specify otherwise.  You can set or clear the bits with symbolic modes like u+s and g-s.  To clear these bits for directories with a numeric mode requires an additional leading zero, or leading = like 00755 , or =755                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
RESTRICTED DELETION FLAG OR STICKY BIT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       The restricted deletion flag or sticky bit is a single bit, whose interpretation depends on the file type.  For directories, it prevents unprivileged users from removing or renaming a file in the directory unless they own the file or the directory; this is called the restricted deletion flag for the directory, and is commonly found on world-writable directo‐                                                                                                                                                                                                                                                                      
       ries like /tmp.  For regular files on some older systems, the bit saves the program's text image on the swap device so it will load more quickly when run; this is called the sticky bit.

OPTIONS
       Change the mode of each FILE to MODE.  With --reference, change the mode of each FILE to that of RFILE.

       -c, --changes
              like verbose but report only when a change is made

       -f, --silent, --quiet
              suppress most error messages

       -v, --verbose
              output a diagnostic for every file processed

       --no-preserve-root
              do not treat '/' specially (the default)

       --preserve-root
              fail to operate recursively on '/'

       --reference=RFILE
              use RFILE's mode instead of MODE values

       -R, --recursive
              change files and directories recursively

       --help display this help and exit

       --version
              output version information and exit

       Each MODE is of the form '[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+'.

AUTHOR
       Written by David MacKenzie and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report chmod translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       chmod(2)

       Full documentation at: <https://www.gnu.org/software/coreutils/chmod>
       or available locally via: info '(coreutils) chmod invocation'

GNU coreutils 8.30                                                                                                                                                                August 2019                                                                                                                                                                          CHMOD(1)

'''

_rm = '''

RM(1)                                                                                                                                                                                                                                                                                                       User Commands                                                                                                                                                                                                                                                                                                       RM(1)

NAME
       rm - remove files or directories

SYNOPSIS
       rm [OPTION]... [FILE]...

DESCRIPTION
       This manual page documents the GNU version of rm.  rm removes each specified file.  By default, it does not remove directories.

       If the -I or --interactive=once option is given, and there are more than three files or the -r, -R, or --recursive are given, then rm prompts the user for whether to proceed with the entire operation.  If the response is not affirmative, the entire command is aborted.

       Otherwise, if a file is unwritable, standard input is a terminal, and the -f or --force option is not given, or the -i or --interactive=always option is given, rm prompts the user for whether to remove the file.  If the response is not affirmative, the file is skipped.

OPTIONS
       Remove (unlink) the FILE(s).

       -f, --force
              ignore nonexistent files and arguments, never prompt

       -i     prompt before every removal

       -I     prompt once before removing more than three files, or when removing recursively; less intrusive than -i, while still giving protection against most mistakes

       --interactive[=WHEN]
              prompt according to WHEN: never, once (-I), or always (-i); without WHEN, prompt always

       --one-file-system
              when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument

       --no-preserve-root
              do not treat '/' specially

       --preserve-root[=all]
              do not remove '/' (default); with 'all', reject any command line argument on a separate device from its parent

       -r, -R, --recursive
              remove directories and their contents recursively

       -d, --dir
              remove empty directories

       -v, --verbose
              explain what is being done

       --help display this help and exit

       --version
              output version information and exit

       By default, rm does not remove directories.  Use the --recursive (-r or -R) option to remove each listed directory, too, along with all of its contents.

       To remove a file whose name starts with a '-', for example '-foo', use one of these commands:

              rm -- -foo

              rm ./-foo

       Note that if you use rm to remove a file, it might be possible to recover some of its contents, given sufficient expertise and/or time.  For greater assurance that the contents are truly unrecoverable, consider using shred.

AUTHOR
       Written by Paul Rubin, David MacKenzie, Richard M. Stallman, and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report rm translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       unlink(1), unlink(2), chattr(1), shred(1)

       Full documentation at: <https://www.gnu.org/software/coreutils/rm>
       or available locally via: info '(coreutils) rm invocation'

GNU coreutils 8.30                                                                                                                                                                                                                                                                                           August 2019                                                                                                                                                                                                                                                                                                        RM(1)

'''

_cp = '''
CP(1)                                                                                                                                                                                                                                                                                                       User Commands                                                                                                                                                                                                                                                                                                       CP(1)                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
       cp - copy files and directories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
SYNOPSIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
       cp [OPTION]... [-T] SOURCE DEST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
       cp [OPTION]... SOURCE... DIRECTORY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
       cp [OPTION]... -t DIRECTORY SOURCE...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
       Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       Mandatory arguments to long options are mandatory for short options too.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -a, --archive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
              same as -dR --preserve=all                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --attributes-only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
              don't copy the file data, just the attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --backup[=CONTROL]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
              make a backup of each existing destination file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -b     like --backup but does not accept an argument                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --copy-contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
              copy contents of special files when recursive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -d     same as --no-dereference --preserve=links                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -f, --force                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
              if an existing destination file cannot be opened, remove it and try again (this option is ignored when the -n option is also used)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -i, --interactive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
              prompt before overwrite (overrides a previous -n option)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -H     follow command-line symbolic links in SOURCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -l, --link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
              hard link files instead of copying                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -L, --dereference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
              always follow symbolic links in SOURCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -n, --no-clobber                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
              do not overwrite an existing file (overrides a previous -i option)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -P, --no-dereference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
              never follow symbolic links in SOURCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -p     same as --preserve=mode,ownership,timestamps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --preserve[=ATTR_LIST]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
              preserve the specified attributes (default: mode,ownership,timestamps), if possible additional attributes: context, links, xattr, all                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --no-preserve=ATTR_LIST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
              don't preserve the specified attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --parents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
              use full source file name under DIRECTORY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       -R, -r, --recursive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
              copy directories recursively                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --reflink[=WHEN]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
              control clone/CoW copies. See below                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       --remove-destination                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
              remove each existing destination file before attempting to open it (contrast with --force)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

       --sparse=WHEN
              control creation of sparse files. See below

       --strip-trailing-slashes
              remove any trailing slashes from each SOURCE argument

       -s, --symbolic-link
              make symbolic links instead of copying

       -S, --suffix=SUFFIX
              override the usual backup suffix

       -t, --target-directory=DIRECTORY
              copy all SOURCE arguments into DIRECTORY

       -T, --no-target-directory
              treat DEST as a normal file

       -u, --update
              copy only when the SOURCE file is newer than the destination file or when the destination file is missing

       -v, --verbose
              explain what is being done

       -x, --one-file-system
              stay on this file system

       -Z     set SELinux security context of destination file to default type

       --context[=CTX]
              like -Z, or if CTX is specified then set the SELinux or SMACK security context to CTX

       --help display this help and exit

       --version
              output version information and exit

       By default, sparse SOURCE files are detected by a crude heuristic and the corresponding DEST file is made sparse as well.  That is the behavior selected by --sparse=auto.  Specify --sparse=always to create a sparse DEST file whenever the SOURCE file contains a long enough sequence of zero bytes.  Use --sparse=never to inhibit creation of sparse files.

       When --reflink[=always] is specified, perform a lightweight copy, where the data blocks are copied only when modified.  If this is not possible the copy fails, or if --reflink=auto is specified, fall back to a standard copy.  Use --reflink=never to ensure a standard copy is performed.

       The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.  The version control method may be selected via the --backup option or through the VERSION_CONTROL environment variable.  Here are the values:

       none, off
              never make backups (even if --backup is given)

       numbered, t
              make numbered backups

       existing, nil
              numbered if numbered backups exist, simple otherwise

       simple, never
              always make simple backups

       As a special case, cp makes a backup of SOURCE when the force and backup options are given and SOURCE and DEST are the same name for an existing, regular file.

AUTHOR
       Written by Torbjorn Granlund, David MacKenzie, and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report cp translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <https://www.gnu.org/software/coreutils/cp>
       or available locally via: info '(coreutils) cp invocation'

GNU coreutils 8.30                                                                                                                                                                                                                                                                                           August 2019                                                                                                                                                                                                                                                                                                        CP(1)

'''



_mkdir = '''
MKDIR(1)                                                                                                                                           User Commands                                                                                                                                          MKDIR(1)

NAME
       mkdir - make directories

SYNOPSIS
       mkdir [OPTION]... DIRECTORY...

DESCRIPTION
       Create the DIRECTORY(ies), if they do not already exist.

       Mandatory arguments to long options are mandatory for short options too.

       -m, --mode=MODE
              set file mode (as in chmod), not a=rwx - umask

       -p, --parents
              no error if existing, make parent directories as needed

       -v, --verbose
              print a message for each created directory

       -Z     set SELinux security context of each created directory to the default type

       --context[=CTX]
              like -Z, or if CTX is specified then set the SELinux or SMACK security context to CTX

       --help display this help and exit

       --version
              output version information and exit

AUTHOR
       Written by David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report mkdir translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       mkdir(2)

       Full documentation at: <https://www.gnu.org/software/coreutils/mkdir>
       or available locally via: info '(coreutils) mkdir invocation'

GNU coreutils 8.30                                                                                                                                  August 2019                                                                                                                                           MKDIR(1)

'''

_ln = '''
LN(1)                                                                                                                                              User Commands                                                                                                                                             LN(1)                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
       ln - make links between files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
SYNOPSIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
       ln [OPTION]... [-T] TARGET LINK_NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
       ln [OPTION]... TARGET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
       ln [OPTION]... TARGET... DIRECTORY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
       ln [OPTION]... -t DIRECTORY TARGET...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
       In  the  1st  form,  create a link to TARGET with the name LINK_NAME.  In the 2nd form, create a link to TARGET in the current directory.  In the 3rd and 4th forms, create links to each TARGET in DIRECTORY.  Create hard links by default, symbolic links with --symbolic.  By default, each destination                                                                                                                                                                                                                                                                                                                                   
       (name of new link) should not already exist.  When creating hard links, each TARGET must exist.  Symbolic links can hold arbitrary text; if later resolved, a relative link is interpreted in relation to its parent directory.                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       Mandatory arguments to long options are mandatory for short options too.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       --backup[=CONTROL]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
              make a backup of each existing destination file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -b     like --backup but does not accept an argument                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -d, -F, --directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
              allow the superuser to attempt to hard link directories (note: will probably fail due to system restrictions, even for the superuser)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -f, --force                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
              remove existing destination files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -i, --interactive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
              prompt whether to remove destinations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -L, --logical                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
              dereference TARGETs that are symbolic links                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
       -n, --no-dereference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
              treat LINK_NAME as a normal file if it is a symbolic link to a directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

       -P, --physical
              make hard links directly to symbolic links

       -r, --relative
              create symbolic links relative to link location

       -s, --symbolic
              make symbolic links instead of hard links

       -S, --suffix=SUFFIX
              override the usual backup suffix

       -t, --target-directory=DIRECTORY
              specify the DIRECTORY in which to create the links

       -T, --no-target-directory
              treat LINK_NAME as a normal file always

       -v, --verbose
              print name of each linked file

       --help display this help and exit

       --version
              output version information and exit

       The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.  The version control method may be selected via the --backup option or through the VERSION_CONTROL environment variable.  Here are the values:

       none, off
              never make backups (even if --backup is given)

       numbered, t
              make numbered backups

       existing, nil
              numbered if numbered backups exist, simple otherwise

       simple, never
              always make simple backups

       Using -s ignores -L and -P.  Otherwise, the last option specified controls behavior when a TARGET is a symbolic link, defaulting to -P.

AUTHOR
       Written by Mike Parker and David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report ln translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2018 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       link(2), symlink(2)

       Full documentation at: <https://www.gnu.org/software/coreutils/ln>
       or available locally via: info '(coreutils) ln invocation'

GNU coreutils 8.30                                                                                                                                  August 2019                                                                                                                                              LN(1)

'''



_grep = '''
GREP(1)                                                                                                                      User Commands                                                                                                                     GREP(1)

NAME
       grep, egrep, fgrep, rgrep - print lines that match patterns

SYNOPSIS
       grep [OPTION...] PATTERNS [FILE...]
       grep [OPTION...] -e PATTERNS ... [FILE...]
       grep [OPTION...] -f PATTERN_FILE ... [FILE...]

DESCRIPTION
       grep searches for PATTERNS in each FILE.  PATTERNS is one or more patterns separated by newline characters, and grep prints each line that matches a pattern.  Typically PATTERNS should be quoted when grep is used in a shell command.

       A FILE of “-” stands for standard input.  If no FILE is given, recursive searches examine the working directory, and nonrecursive searches read standard input.

       In addition, the variant programs egrep, fgrep and rgrep are the same as grep -E, grep -F, and grep -r, respectively.  These variants are deprecated, but are provided for backward compatibility.

OPTIONS
   Generic Program Information
       --help Output a usage message and exit.

       -V, --version
              Output the version number of grep and exit.

   Pattern Syntax
       -E, --extended-regexp
              Interpret PATTERNS as extended regular expressions (EREs, see below).

       -F, --fixed-strings
              Interpret PATTERNS as fixed strings, not regular expressions.

       -G, --basic-regexp
              Interpret PATTERNS as basic regular expressions (BREs, see below).  This is the default.

       -P, --perl-regexp
              Interpret PATTERNS as Perl-compatible regular expressions (PCREs).  This option is experimental when combined with the -z (--null-data) option, and grep -P may warn of unimplemented features.

   Matching Control
       -e PATTERNS, --regexp=PATTERNS
              Use PATTERNS as the patterns.  If this option is used multiple times or is combined with the -f (--file) option, search for all patterns given.  This option can be used to protect a pattern beginning with “-”.

       -f FILE, --file=FILE
              Obtain patterns from FILE, one per line.  If this option is used multiple times or is combined with the -e (--regexp) option, search for all patterns given.  The empty file contains zero patterns, and therefore matches nothing.

       -i, --ignore-case
              Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.

       --no-ignore-case
              Do not ignore case distinctions in patterns and input data.  This is the default.  This option is useful for passing to shell scripts that already use -i, to cancel its effects because the two options override each other.

       -v, --invert-match
              Invert the sense of matching, to select non-matching lines.

       -w, --word-regexp
              Select only those lines containing matches that form whole words.  The test is that the matching substring must either be at the beginning of the line, or preceded by a non-word constituent character.  Similarly, it must be either at the end of the
              line or followed by a non-word constituent character.  Word-constituent characters are letters, digits, and the underscore.  This option has no effect if -x is also specified.

       -x, --line-regexp
              Select only those matches that exactly match the whole line.  For a regular expression pattern, this is like parenthesizing the pattern and then surrounding it with ^ and $.

       -y     Obsolete synonym for -i.

   General Output Control
       -c, --count
              Suppress normal output; instead print a count of matching lines for each input file.  With the -v, --invert-match option (see below), count non-matching lines.

       --color[=WHEN], --colour[=WHEN]
              Surround the matched (non-empty) strings, matching lines, context lines, file names, line numbers, byte offsets, and separators (for fields and groups of context lines) with escape sequences to display them in color on the terminal.  The colors are
              defined by the environment variable GREP_COLORS.  The deprecated environment variable GREP_COLOR is still supported, but its setting does not have priority.  WHEN is never, always, or auto.

       -L, --files-without-match
              Suppress normal output; instead print the name of each input file from which no output would normally have been printed.  The scanning will stop on the first match.

       -l, --files-with-matches
              Suppress normal output; instead print the name of each input file from which output would normally have been printed.  The scanning will stop on the first match.

       -m NUM, --max-count=NUM
              Stop reading a file after NUM matching lines.  If the input is standard input from a regular file, and NUM matching lines are output, grep ensures that the standard input is positioned to just after the last matching line before exiting, regardless
              of the presence of trailing context lines.  This enables a calling process to resume a search.  When grep stops after NUM matching lines, it outputs any trailing context lines.  When the -c or --count option is also used, grep  does  not  output  a
              count greater than NUM.  When the -v or --invert-match option is also used, grep stops after outputting NUM non-matching lines.

       -o, --only-matching
              Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.

       -q, --quiet, --silent
              Quiet; do not write anything to standard output.  Exit immediately with zero status if any match is found, even if an error was detected.  Also see the -s or --no-messages option.

       -s, --no-messages
              Suppress error messages about nonexistent or unreadable files.

   Output Line Prefix Control
       -b, --byte-offset
              Print the 0-based byte offset within the input file before each line of output.  If -o (--only-matching) is specified, print the offset of the matching part itself.

       -H, --with-filename
              Print the file name for each match.  This is the default when there is more than one file to search.

       -h, --no-filename
              Suppress the prefixing of file names on output.  This is the default when there is only one file (or only standard input) to search.

       --label=LABEL
              Display  input  actually  coming  from  standard input as input coming from file LABEL.  This can be useful for commands that transform a file's contents before searching, e.g., gzip -cd foo.gz | grep --label=foo -H 'some pattern'.  See also the -H
              option.

       -n, --line-number
              Prefix each line of output with the 1-based line number within its input file.

       -T, --initial-tab
              Make sure that the first character of actual line content lies on a tab stop, so that the alignment of tabs looks normal.  This is useful with options that prefix their output to the  actual  content:  -H,-n,  and  -b.   In  order  to  improve  the
              probability that lines from a single file will all start at the same column, this also causes the line number and byte offset (if present) to be printed in a minimum size field width.

       -u, --unix-byte-offsets
              Report  Unix-style byte offsets.  This switch causes grep to report byte offsets as if the file were a Unix-style text file, i.e., with CR characters stripped off.  This will produce results identical to running grep on a Unix machine.  This option
              has no effect unless -b option is also used; it has no effect on platforms other than MS-DOS and MS-Windows.

       -Z, --null
              Output a zero byte (the ASCII NUL character) instead of the character that normally follows a file name.  For example, grep -lZ outputs a zero byte after each file name instead of the usual newline.  This option makes the output  unambiguous,  even
              in the presence of file names containing unusual characters like newlines.  This option can be used with commands like find -print0, perl -0, sort -z, and xargs -0 to process arbitrary file names, even those that contain newline characters.

   Context Line Control
       -A NUM, --after-context=NUM
              Print NUM lines of trailing context after matching lines.  Places a line containing a group separator (--) between contiguous groups of matches.  With the -o or --only-matching option, this has no effect and a warning is given.

       -B NUM, --before-context=NUM
              Print NUM lines of leading context before matching lines.  Places a line containing a group separator (--) between contiguous groups of matches.  With the -o or --only-matching option, this has no effect and a warning is given.

       -C NUM, -NUM, --context=NUM
              Print NUM lines of output context.  Places a line containing a group separator (--) between contiguous groups of matches.  With the -o or --only-matching option, this has no effect and a warning is given.

   File and Directory Selection
       -a, --text
              Process a binary file as if it were text; this is equivalent to the --binary-files=text option.

       --binary-files=TYPE
              If  a  file's  data or metadata indicate that the file contains binary data, assume that the file is of type TYPE.  Non-text bytes indicate binary data; these are either output bytes that are improperly encoded for the current locale, or null input
              bytes when the -z option is not given.

              By default, TYPE is binary, and grep suppresses output after null input binary data is discovered, and suppresses output lines that contain improperly encoded data.  When some output is suppressed, grep follows any output with  a  one-line  message
              saying that a binary file matches.

              If TYPE is without-match, when grep discovers null input binary data it assumes that the rest of the file does not match; this is equivalent to the -I option.

              If TYPE is text, grep processes a binary file as if it were text; this is equivalent to the -a option.

              When  type  is binary, grep may treat non-text bytes as line terminators even without the -z option.  This means choosing binary versus text can affect whether a pattern matches a file.  For example, when type is binary the pattern q$ might match q
              immediately followed by a null byte, even though this is not matched when type is text.  Conversely, when type is binary the pattern . (period) might not match a null byte.

              Warning: The -a option might output binary garbage, which can have nasty side effects if the output is a terminal and if the terminal driver interprets some of it as commands.  On the other hand, when reading files whose text encodings are unknown,
              it can be helpful to use -a or to set LC_ALL='C' in the environment, in order to find more matches even if the matches are unsafe for direct display.

       -D ACTION, --devices=ACTION
              If an input file is a device, FIFO or socket, use ACTION to process it.  By default, ACTION is read, which means that devices are read just as if they were ordinary files.  If ACTION is skip, devices are silently skipped.

       -d ACTION, --directories=ACTION
              If  an  input  file  is  a directory, use ACTION to process it.  By default, ACTION is read, i.e., read directories just as if they were ordinary files.  If ACTION is skip, silently skip directories.  If ACTION is recurse, read all files under each
              directory, recursively, following symbolic links only if they are on the command line.  This is equivalent to the -r option.

       --exclude=GLOB
              Skip any command-line file with a name suffix that matches the pattern GLOB, using wildcard matching; a name suffix is either the whole name, or a trailing part that starts with a non-slash character immediately after a slash (/) in the name.  When
              searching recursively, skip any subfile whose base name matches GLOB; the base name is the part after the last slash.  A pattern can use *, ?, and [...] as wildcards, and \ to quote a wildcard or backslash character literally.

       --exclude-from=FILE
              Skip files whose base name matches any of the file-name globs read from FILE (using wildcard matching as described under --exclude).

       --exclude-dir=GLOB
              Skip any command-line directory with a name suffix that matches the pattern GLOB.  When searching recursively, skip any subdirectory whose base name matches GLOB.  Ignore any redundant trailing slashes in GLOB.

       -I     Process a binary file as if it did not contain matching data; this is equivalent to the --binary-files=without-match option.

       --include=GLOB
              Search only files whose base name matches GLOB (using wildcard matching as described under --exclude).

       -r, --recursive
              Read all files under each directory, recursively, following symbolic links only if they are on the command line.  Note that if no file operand is given, grep searches the working directory.  This is equivalent to the -d recurse option.

       -R, --dereference-recursive
              Read all files under each directory, recursively.  Follow all symbolic links, unlike -r.

   Other Options
       --line-buffered
              Use line buffering on output.  This can cause a performance penalty.

       -U, --binary
              Treat the file(s) as binary.  By default, under MS-DOS and MS-Windows, grep guesses whether a file is text or binary as described for the --binary-files option.  If grep decides the file is a text file, it strips the CR characters from the original
              file contents (to make regular expressions with ^ and $ work correctly).  Specifying -U overrules this guesswork, causing all files to be read and passed to the matching mechanism verbatim; if the file is a text file with CR/LF pairs at the end  of
              each line, this will cause some regular expressions to fail.  This option has no effect on platforms other than MS-DOS and MS-Windows.

       -z, --null-data
              Treat input and output data as sequences of lines, each terminated by a zero byte (the ASCII NUL character) instead of a newline.  Like the -Z or --null option, this option can be used with commands like sort -z to process arbitrary file names.

REGULAR EXPRESSIONS
       A regular expression is a pattern that describes a set of strings.  Regular expressions are constructed analogously to arithmetic expressions, by using various operators to combine smaller expressions.

       grep understands three different versions of regular expression syntax: “basic” (BRE), “extended” (ERE) and “perl” (PCRE).  In GNU grep there is no difference in available functionality between basic and extended syntaxes.  In other implementations, basic
       regular expressions are less powerful.  The following description applies to extended regular expressions; differences for basic regular expressions are summarized afterwards.  Perl-compatible regular expressions give  additional  functionality,  and  are
       documented in pcresyntax(3) and pcrepattern(3), but work only if PCRE is available in the system.

       The  fundamental  building  blocks  are  the  regular  expressions  that match a single character.  Most characters, including all letters and digits, are regular expressions that match themselves.  Any meta-character with special meaning may be quoted by
       preceding it with a backslash.

       The period . matches any single character.  It is unspecified whether it matches an encoding error.

   Character Classes and Bracket Expressions
       A bracket expression is a list of characters enclosed by [ and ].  It matches any single character in that list.  If the first character of the list is the caret ^ then it matches any character not in the list; it is  unspecified  whether  it  matches  an
       encoding error.  For example, the regular expression [0123456789] matches any single digit.

       Within  a bracket expression, a range expression consists of two characters separated by a hyphen.  It matches any single character that sorts between the two characters, inclusive, using the locale's collating sequence and character set.  For example, in
       the default C locale, [a-d] is equivalent to [abcd].  Many locales sort characters in dictionary order, and in these locales [a-d] is typically not equivalent to [abcd]; it might be  equivalent  to  [aBbCcDd],  for  example.   To  obtain  the  traditional
       interpretation of bracket expressions, you can use the C locale by setting the LC_ALL environment variable to the value C.

       Finally,  certain  named  classes  of  characters  are  predefined  within  bracket expressions, as follows.  Their names are self explanatory, and they are [:alnum:], [:alpha:], [:blank:], [:cntrl:], [:digit:], [:graph:], [:lower:], [:print:], [:punct:],
       [:space:], [:upper:], and [:xdigit:].  For example, [[:alnum:]] means the character class of numbers and letters in the current locale.  In the C locale and ASCII character set encoding, this is the same as [0-9A-Za-z].  (Note that the brackets  in  these
       class  names  are  part  of the symbolic names, and must be included in addition to the brackets delimiting the bracket expression.)  Most meta-characters lose their special meaning inside bracket expressions.  To include a literal ] place it first in the
       list.  Similarly, to include a literal ^ place it anywhere but first.  Finally, to include a literal - place it last.

   Anchoring
       The caret ^ and the dollar sign $ are meta-characters that respectively match the empty string at the beginning and end of a line.

   The Backslash Character and Special Expressions
       The symbols \< and \> respectively match the empty string at the beginning and end of a word.  The symbol \b matches the empty string at the edge of a word, and \B matches the empty string provided it's not at the edge of a  word.   The  symbol  \w  is  a
       synonym for [_[:alnum:]] and \W is a synonym for [^_[:alnum:]].

   Repetition
       A regular expression may be followed by one of several repetition operators:
       ?      The preceding item is optional and matched at most once.
       *      The preceding item will be matched zero or more times.
       +      The preceding item will be matched one or more times.
       {n}    The preceding item is matched exactly n times.
       {n,}   The preceding item is matched n or more times.
       {,m}   The preceding item is matched at most m times.  This is a GNU extension.
       {n,m}  The preceding item is matched at least n times, but not more than m times.

   Concatenation
       Two regular expressions may be concatenated; the resulting regular expression matches any string formed by concatenating two substrings that respectively match the concatenated expressions.

   Alternation
       Two regular expressions may be joined by the infix operator |; the resulting regular expression matches any string matching either alternate expression.

   Precedence
       Repetition takes precedence over concatenation, which in turn takes precedence over alternation.  A whole expression may be enclosed in parentheses to override these precedence rules and form a subexpression.

   Back-references and Subexpressions
       The back-reference \n, where n is a single digit, matches the substring previously matched by the nth parenthesized subexpression of the regular expression.

   Basic vs Extended Regular Expressions
       In basic regular expressions the meta-characters ?, +, {, |, (, and ) lose their special meaning; instead use the backslashed versions \?, \+, \{, \|, \(, and \).

EXIT STATUS
       Normally the exit status is 0 if a line is selected, 1 if no lines were selected, and 2 if an error occurred.  However, if the -q or --quiet or --silent is used and a line is selected, the exit status is 0 even if an error occurred.

ENVIRONMENT
       The behavior of grep is affected by the following environment variables.

       The  locale  for  category  LC_foo is specified by examining the three environment variables LC_ALL, LC_foo, LANG, in that order.  The first of these variables that is set specifies the locale.  For example, if LC_ALL is not set, but LC_MESSAGES is set to
       pt_BR, then the Brazilian Portuguese locale is used for the LC_MESSAGES category.  The C locale is used if none of these environment variables are set, if the locale catalog is not installed, or if grep was not  compiled  with  national  language  support
       (NLS).  The shell command locale -a lists locales that are currently available.

       GREP_OPTIONS
              This  variable  specifies  default options to be placed in front of any explicit options.  As this causes problems when writing portable scripts, this feature will be removed in a future release of grep, and grep warns if it is used.  Please use an
              alias or script instead.

       GREP_COLOR
              This variable specifies the color used to highlight matched (non-empty) text.  It is deprecated in favor of GREP_COLORS, but still supported.  The mt, ms, and mc capabilities of GREP_COLORS have priority over it.  It can only specify the color used
              to  highlight  the  matching  non-empty  text in any matching line (a selected line when the -v command-line option is omitted, or a context line when -v is specified).  The default is 01;31, which means a bold red foreground text on the terminal's
              default background.

       GREP_COLORS
              Specifies the colors and other attributes used to highlight various parts of the output.  Its value is a colon-separated list of capabilities that defaults to ms=01;31:mc=01;31:sl=:cx=:fn=35:ln=32:bn=32:se=36 with the rv and ne boolean capabilities
              omitted (i.e., false).  Supported capabilities are as follows.

              sl=    SGR substring for whole selected lines (i.e., matching lines when the -v command-line option is omitted, or non-matching lines when -v is specified).  If however the boolean rv capability and the -v command-line option are both specified, it
                     applies to context matching lines instead.  The default is empty (i.e., the terminal's default color pair).

              cx=    SGR substring for whole context lines (i.e., non-matching lines when the -v command-line option is omitted, or matching lines when -v is specified).  If however the boolean rv capability and the -v command-line option are both specified,  it
                     applies to selected non-matching lines instead.  The default is empty (i.e., the terminal's default color pair).

              rv     Boolean value that reverses (swaps) the meanings of the sl= and cx= capabilities when the -v command-line option is specified.  The default is false (i.e., the capability is omitted).

              mt=01;31
                     SGR substring for matching non-empty text in any matching line (i.e., a selected line when the -v command-line option is omitted, or a context line when -v is specified).  Setting this is equivalent to setting both ms= and mc= at once to the
                     same value.  The default is a bold red text foreground over the current line background.

              ms=01;31
                     SGR substring for matching non-empty text in a selected line.  (This is only used when the -v command-line option is omitted.)  The effect of the sl= (or cx= if rv) capability remains active when this kicks in.  The default  is  a  bold  red
                     text foreground over the current line background.

              mc=01;31
                     SGR  substring  for  matching non-empty text in a context line.  (This is only used when the -v command-line option is specified.)  The effect of the cx= (or sl= if rv) capability remains active when this kicks in.  The default is a bold red
                     text foreground over the current line background.

              fn=35  SGR substring for file names prefixing any content line.  The default is a magenta text foreground over the terminal's default background.

              ln=32  SGR substring for line numbers prefixing any content line.  The default is a green text foreground over the terminal's default background.

              bn=32  SGR substring for byte offsets prefixing any content line.  The default is a green text foreground over the terminal's default background.

              se=36  SGR substring for separators that are inserted between selected line fields (:), between context line fields, (-), and between groups of adjacent lines when nonzero context is specified (--).  The default is a cyan text foreground  over  the
                     terminal's default background.

              ne     Boolean  value that prevents clearing to the end of line using Erase in Line (EL) to Right (\33[K) each time a colorized item ends.  This is needed on terminals on which EL is not supported.  It is otherwise useful on terminals for which the
                     back_color_erase (bce) boolean terminfo capability does not apply, when the chosen highlight colors do not affect the background, or when EL is too slow or causes too much flicker.  The default is false (i.e., the capability is omitted).

              Note that boolean capabilities have no =... part.  They are omitted (i.e., false) by default and become true when specified.

              See the Select Graphic Rendition (SGR) section in the documentation of the text terminal that is used for permitted values and their meaning as character attributes.  These substring  values  are  integers  in  decimal  representation  and  can  be
              concatenated  with  semicolons.  grep takes care of assembling the result into a complete SGR sequence (\33[...m).  Common values to concatenate include 1 for bold, 4 for underline, 5 for blink, 7 for inverse, 39 for default foreground color, 30 to
              37 for foreground colors, 90 to 97 for 16-color mode foreground colors, 38;5;0 to 38;5;255 for 88-color and 256-color modes foreground colors, 49 for default background color, 40 to 47 for background colors, 100 to 107 for 16-color mode  background
              colors, and 48;5;0 to 48;5;255 for 88-color and 256-color modes background colors.

       LC_ALL, LC_COLLATE, LANG
              These variables specify the locale for the LC_COLLATE category, which determines the collating sequence used to interpret range expressions like [a-z].

       LC_ALL, LC_CTYPE, LANG
              These  variables  specify the locale for the LC_CTYPE category, which determines the type of characters, e.g., which characters are whitespace.  This category also determines the character encoding, that is, whether text is encoded in UTF-8, ASCII,
              or some other encoding.  In the C or POSIX locale, all characters are encoded as a single byte and every byte is a valid character.

       LC_ALL, LC_MESSAGES, LANG
              These variables specify the locale for the LC_MESSAGES category, which determines the language that grep uses for messages.  The default C locale uses American English messages.

       POSIXLY_CORRECT
              If set, grep behaves as POSIX requires; otherwise, grep behaves more like other GNU programs.  POSIX requires that options that follow file names must be treated as file names; by default, such options are permuted to the front of the operand  list
              and  are  treated  as  options.   Also,  POSIX  requires  that  unrecognized  options  be  diagnosed  as  “illegal”,  but  since  they  are  not  really  against  the  law the default is to diagnose them as “invalid”.  POSIXLY_CORRECT also disables
              _N_GNU_nonoption_argv_flags_, described below.

       _N_GNU_nonoption_argv_flags_
              (Here N is grep's numeric process ID.)  If the ith character of this environment variable's value is 1, do not consider the ith operand of grep to be an option, even if it appears to be one.  A shell can put this variable  in  the  environment  for
              each command it runs, specifying which operands are the results of file name wildcard expansion and therefore should not be treated as options.  This behavior is available only with the GNU C library, and only when POSIXLY_CORRECT is not set.

NOTES
       This man page is maintained only fitfully; the full documentation is often more up-to-date.

COPYRIGHT
       Copyright 1998-2000, 2002, 2005-2020 Free Software Foundation, Inc.

       This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

BUGS
   Reporting Bugs
       Email bug reports to the bug-reporting address ⟨bug-grep@gnu.org⟩.  An email archive ⟨https://lists.gnu.org/mailman/listinfo/bug-grep⟩ and a bug tracker ⟨https://debbugs.gnu.org/cgi/pkgreport.cgi?package=grep⟩ are available.

   Known Bugs
       Large repetition counts in the {n,m} construct may cause grep to use lots of memory.  In addition, certain other obscure regular expressions require exponential time and space, and may cause grep to run out of memory.

       Back-references are very slow, and may require exponential time.

EXAMPLE
       The  following  example  outputs the location and contents of any line containing “f” and ending in “.c”, within all files in the current directory whose names contain “g” and end in “.h”.  The -n option outputs line numbers, the -- argument treats expan‐
       sions of “*g*.h” starting with “-” as file names not options, and the empty file /dev/null causes file names to be output even if only one file name happens to be of the form “*g*.h”.

         $ grep -n -- 'f.*\.c$' *g*.h /dev/null
         argmatch.h:1:/* definitions and prototypes for argmatch.c

       The only line that matches is line 1 of argmatch.h.  Note that the regular expression syntax used in the pattern differs from the globbing syntax that the shell uses to match file names.

SEE ALSO
   Regular Manual Pages
       awk(1), cmp(1), diff(1), find(1), perl(1), sed(1), sort(1), xargs(1), read(2), pcre(3), pcresyntax(3), pcrepattern(3), terminfo(5), glob(7), regex(7).

   Full Documentation
       A complete manual ⟨https://www.gnu.org/software/grep/manual/⟩ is available.  If the info and grep programs are properly installed at your site, the command

              info grep

       should give you access to the complete manual.

GNU grep 3.4                                                                                                                  2019-12-29                                                                                                                       GREP(1)

'''

_sudo = '''
(8)                                                                                                               BSD System Manager's Manual                                                                                                              SUDO(8)

NAME
     sudo, sudoedit — execute a command as another user

SYNOPSIS
     sudo -h | -K | -k | -V
     sudo -v [-ABknS] [-g group] [-h host] [-p prompt] [-u user]
     sudo -l [-ABknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
     sudo [-ABbEHnPS] [-C num] [-g group] [-h host] [-p prompt] [-r role] [-t type] [-T timeout] [-u user] [VAR=value] [-i | -s] [command]
     sudoedit [-ABknS] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...

DESCRIPTION
     sudo allows a permitted user to execute a command as the superuser or another user, as specified by the security policy.  The invoking user's real (not effective) user-ID is used to determine the user name with which to query the security policy.

     sudo supports a plugin architecture for security policies and input/output logging.  Third parties can develop and distribute their own policy and I/O logging plugins to work seamlessly with the sudo front end.  The default security policy is sudoers, which
     is configured via the file /etc/sudoers, or via LDAP.  See the Plugins section for more information.

     The security policy determines what privileges, if any, a user has to run sudo.  The policy may require that users authenticate themselves with a password or another authentication mechanism.  If authentication is required, sudo will exit if the user's
     password is not entered within a configurable time limit.  This limit is policy-specific; the default password prompt timeout for the sudoers security policy is 0 minutes.

     Security policies may support credential caching to allow the user to run sudo again for a period of time without requiring authentication.  By default, the sudoers policy caches credentials on a per-terminal basis for 15 minutes.  See the timestamp_type
     and timestamp_timeout options in sudoers(5) for more information.  By running sudo with the -v option, a user can update the cached credentials without running a command.

     When invoked as sudoedit, the -e option (described below), is implied.

     Security policies may log successful and failed attempts to use sudo.  If an I/O plugin is configured, the running command's input and output may be logged as well.

     The options are as follows:

     -A, --askpass
                 Normally, if sudo requires a password, it will read it from the user's terminal.  If the -A (askpass) option is specified, a (possibly graphical) helper program is executed to read the user's password and output the password to the standard out‐
                 put.  If the SUDO_ASKPASS environment variable is set, it specifies the path to the helper program.  Otherwise, if sudo.conf(5) contains a line specifying the askpass program, that value will be used.  For example:

                     # Path to askpass helper program
                     Path askpass /usr/X11R6/bin/ssh-askpass

                 If no askpass program is available, sudo will exit with an error.

     -B, --bell  Ring the bell as part of the password promp when a terminal is present.  This option has no effect if an askpass program is used.

     -b, --background
                 Run the given command in the background.  Note that it is not possible to use shell job control to manipulate background processes started by sudo.  Most interactive commands will fail to work properly in background mode.

     -C num, --close-from=num
                 Close all file descriptors greater than or equal to num before executing a command.  Values less than three are not permitted.  By default, sudo will close all open file descriptors other than standard input, standard output and standard error
                 when executing a command.  The security policy may restrict the user's ability to use this option.  The sudoers policy only permits use of the -C option when the administrator has enabled the closefrom_override option.

     -E, --preserve-env
                 Indicates to the security policy that the user wishes to preserve their existing environment variables.  The security policy may return an error if the user does not have permission to preserve the environment.

     --preserve-env=list
                 Indicates to the security policy that the user wishes to add the comma-separated list of environment variables to those preserved from the user's environment.  The security policy may return an error if the user does not have permission to pre‐
                 serve the environment.  This option may be specified multiple times.

     -e, --edit  Edit one or more files instead of running a command.  In lieu of a path name, the string "sudoedit" is used when consulting the security policy.  If the user is authorized by the policy, the following steps are taken:

                 1.   Temporary copies are made of the files to be edited with the owner set to the invoking user.

                 2.   The editor specified by the policy is run to edit the temporary files.  The sudoers policy uses the SUDO_EDITOR, VISUAL and EDITOR environment variables (in that order).  If none of SUDO_EDITOR, VISUAL or EDITOR are set, the first program
                      listed in the editor sudoers(5) option is used.

                 3.   If they have been modified, the temporary files are copied back to their original location and the temporary versions are removed.

                 To help prevent the editing of unauthorized files, the following restrictions are enforced unless explicitly allowed by the security policy:

                 •  Symbolic links may not be edited (version 1.8.15 and higher).

                 •  Symbolic links along the path to be edited are not followed when the parent directory is writable by the invoking user unless that user is root (version 1.8.16 and higher).

                 •  Files located in a directory that is writable by the invoking user may not be edited unless that user is root (version 1.8.16 and higher).

                 Users are never allowed to edit device special files.

                 If the specified file does not exist, it will be created.  Note that unlike most commands run by sudo, the editor is run with the invoking user's environment unmodified.  If, for some reason, sudo is unable to update a file with its edited ver‐
                 sion, the user will receive a warning and the edited copy will remain in a temporary file.

     -g group, --group=group
                 Run the command with the primary group set to group instead of the primary group specified by the target user's password database entry.  The group may be either a group name or a numeric group-ID (GID) prefixed with the ‘#’ character (e.g., #0
                 for GID 0).  When running a command as a GID, many shells require that the ‘#’ be escaped with a backslash (‘\’).  If no -u option is specified, the command will be run as the invoking user.  In either case, the primary group will be set to
                 group.  The sudoers policy permits any of the target user's groups to be specified via the -g option as long as the -P option is not in use.

     -H, --set-home
                 Request that the security policy set the HOME environment variable to the home directory specified by the target user's password database entry.  Depending on the policy, this may be the default behavior.

     -h, --help  Display a short help message to the standard output and exit.

     -h host, --host=host
                 Run the command on the specified host if the security policy plugin supports remote commands.  Note that the sudoers plugin does not currently support running remote commands.  This may also be used in conjunction with the -l option to list a
                 user's privileges for the remote host.

     -i, --login
                 Run the shell specified by the target user's password database entry as a login shell.  This means that login-specific resource files such as .profile, .bash_profile or .login will be read by the shell.  If a command is specified, it is passed
                 to the shell for execution via the shell's -c option.  If no command is specified, an interactive shell is executed.  sudo attempts to change to that user's home directory before running the shell.  The command is run with an environment similar
                 to the one a user would receive at log in.  Note that most shells behave differently when a command is specified as compared to an interactive session; consult the shell's manual for details.  The Command environment section in the sudoers(5)
                 manual documents how the -i option affects the environment in which a command is run when the sudoers policy is in use.

     -K, --remove-timestamp
                 Similar to the -k option, except that it removes the user's cached credentials entirely and may not be used in conjunction with a command or other option.  This option does not require a password.  Not all security policies support credential
                 caching.

     -k, --reset-timestamp
                 When used without a command, invalidates the user's cached credentials.  In other words, the next time sudo is run a password will be required.  This option does not require a password and was added to allow a user to revoke sudo permissions
                 from a .logout file.

                 When used in conjunction with a command or an option that may require a password, this option will cause sudo to ignore the user's cached credentials.  As a result, sudo will prompt for a password (if one is required by the security policy) and
                 will not update the user's cached credentials.

                 Not all security policies support credential caching.

     -l, --list  If no command is specified, list the allowed (and forbidden) commands for the invoking user (or the user specified by the -U option) on the current host.  A longer list format is used if this option is specified multiple times and the security
                 policy supports a verbose output format.

                 If a command is specified and is permitted by the security policy, the fully-qualified path to the command is displayed along with any command line arguments.  If a command is specified but not allowed by the policy, sudo will exit with a status
                 value of 1.

     -n, --non-interactive
                 Avoid prompting the user for input of any kind.  If a password is required for the command to run, sudo will display an error message and exit.

     -P, --preserve-groups
                 Preserve the invoking user's group vector unaltered.  By default, the sudoers policy will initialize the group vector to the list of groups the target user is a member of.  The real and effective group-IDs, however, are still set to match the
                 target user.

     -p prompt, --prompt=prompt
                 Use a custom password prompt with optional escape sequences.  The following percent (‘%’) escape sequences are supported by the sudoers policy:

                 %H  expanded to the host name including the domain name (on if the machine's host name is fully qualified or the fqdn option is set in sudoers(5))

                 %h  expanded to the local host name without the domain name

                 %p  expanded to the name of the user whose password is being requested (respects the rootpw, targetpw, and runaspw flags in sudoers(5))

                 %U  expanded to the login name of the user the command will be run as (defaults to root unless the -u option is also specified)

                 %u  expanded to the invoking user's login name

                 %%  two consecutive ‘%’ characters are collapsed into a single ‘%’ character

                 The custom prompt will override the default prompt specified by either the security policy or the SUDO_PROMPT environment variable.  On systems that use PAM, the custom prompt will also override the prompt specified by a PAM module unless the
                 passprompt_override flag is disabled in sudoers.

     -r role, --role=role
                 Run the command with an SELinux security context that includes the specified role.

     -S, --stdin
                 Write the prompt to the standard error and read the password from the standard input instead of using the terminal device.

     -s, --shell
                 Run the shell specified by the SHELL environment variable if it is set or the shell specified by the invoking user's password database entry.  If a command is specified, it is passed to the shell for execution via the shell's -c option.  If no
                 command is specified, an interactive shell is executed.  Note that most shells behave differently when a command is specified as compared to an interactive session; consult the shell's manual for details.

     -t type, --type=type
                 Run the command with an SELinux security context that includes the specified type.  If no type is specified, the default type is derived from the role.

     -U user, --other-user=user
                 Used in conjunction with the -l option to list the privileges for user instead of for the invoking user.  The security policy may restrict listing other users' privileges.  The sudoers policy only allows root or a user with the ALL privilege on
                 the current host to use this option.

     -T timeout, --command-timeout=timeout
                 Used to set a timeout for the command.  If the timeout expires before the command has exited, the command will be terminated.  The security policy may restrict the ability to set command timeouts.  The sudoers policy requires that user-specified
                 timeouts be explicitly enabled.

     -u user, --user=user
                 Run the command as a user other than the default target user (usually root).  The user may be either a user name or a numeric user-ID (UID) prefixed with the ‘#’ character (e.g., #0 for UID 0).  When running commands as a UID, many shells re‐
                 quire that the ‘#’ be escaped with a backslash (‘\’).  Some security policies may restrict UIDs to those listed in the password database.  The sudoers policy allows UIDs that are not in the password database as long as the targetpw option is not
                 set.  Other security policies may not support this.

     -V, --version
                 Print the sudo version string as well as the version string of the security policy plugin and any I/O plugins.  If the invoking user is already root the -V option will display the arguments passed to configure when sudo was built and plugins may
                 display more verbose information such as default options.

     -v, --validate
                 Update the user's cached credentials, authenticating the user if necessary.  For the sudoers plugin, this extends the sudo timeout for another 15 minutes by default, but does not run a command.  Not all security policies support cached creden‐
                 tials.

     --          The -- option indicates that sudo should stop processing command line arguments.

     Options that take a value may only be specified once unless otherwise indicated in the description.  This is to help guard against problems caused by poorly written scripts that invoke sudo with user-controlled input.

     Environment variables to be set for the command may also be passed on the command line in the form of VAR=value, e.g., LD_LIBRARY_PATH=/usr/local/pkg/lib.  Variables passed on the command line are subject to restrictions imposed by the security policy
     plugin.  The sudoers policy subjects variables passed on the command line to the same restrictions as normal environment variables with one important exception.  If the setenv option is set in sudoers, the command to be run has the SETENV tag set or the
     command matched is ALL, the user may set variables that would otherwise be forbidden.  See sudoers(5) for more information.

COMMAND EXECUTION
     When sudo executes a command, the security policy specifies the execution environment for the command.  Typically, the real and effective user and group and IDs are set to match those of the target user, as specified in the password database, and the group
     vector is initialized based on the group database (unless the -P option was specified).

     The following parameters may be specified by security policy:

     •  real and effective user-ID

     •  real and effective group-ID

     •  supplementary group-IDs

     •  the environment list

     •  current working directory

     •  file creation mode mask (umask)

     •  SELinux role and type

     •  scheduling priority (aka nice value)

   Process model
     There are two distinct ways sudo can run a command.

     If an I/O logging plugin is configured or if the security policy explicitly requests it, a new pseudo-terminal (“pty”) is allocated and fork(2) is used to create a second sudo process, referred to as the monitor.  The monitor creates a new terminal session
     with itself as the leader and the pty as its controlling terminal, calls fork(2), sets up the execution environment as described above, and then uses the execve(2) system call to run the command in the child process.  The monitor exists to relay job control
     signals between the user's existing terminal and the pty the command is being run in.  This makes it possible to suspend and resume the command.  Without the monitor, the command would be in what POSIX terms an “orphaned process group” and it would not re‐
     ceive any job control signals from the kernel.  When the command exits or is terminated by a signal, the monitor passes the command's exit status to the main sudo process and exits.  After receiving the command's exit status, the main sudo passes the com‐
     mand's exit status to the security policy's close function and exits.

     If no pty is used, sudo calls fork(2), sets up the execution environment as described above, and uses the execve(2) system call to run the command in the child process.  The main sudo process waits until the command has completed, then passes the command's
     exit status to the security policy's close function and exits.  As a special case, if the policy plugin does not define a close function, sudo will execute the command directly instead of calling fork(2) first.  The sudoers policy plugin will only define a
     close function when I/O logging is enabled, a pty is required, or the pam_session or pam_setcred options are enabled.  Note that pam_session and pam_setcred are enabled by default on systems using PAM.

     On systems that use PAM, the security policy's close function is responsible for closing the PAM session.  It may also log the command's exit status.

   Signal handling
     When the command is run as a child of the sudo process, sudo will relay signals it receives to the command.  The SIGINT and SIGQUIT signals are only relayed when the command is being run in a new pty or when the signal was sent by a user process, not the
     kernel.  This prevents the command from receiving SIGINT twice each time the user enters control-C.  Some signals, such as SIGSTOP and SIGKILL, cannot be caught and thus will not be relayed to the command.  As a general rule, SIGTSTP should be used instead
     of SIGSTOP when you wish to suspend a command being run by sudo.

     As a special case, sudo will not relay signals that were sent by the command it is running.  This prevents the command from accidentally killing itself.  On some systems, the reboot(8) command sends SIGTERM to all non-system processes other than itself be‐
     fore rebooting the system.  This prevents sudo from relaying the SIGTERM signal it received back to reboot(8), which might then exit before the system was actually rebooted, leaving it in a half-dead state similar to single user mode.  Note, however, that
     this check only applies to the command run by sudo and not any other processes that the command may create.  As a result, running a script that calls reboot(8) or shutdown(8) via sudo may cause the system to end up in this undefined state unless the
     reboot(8) or shutdown(8) are run using the exec() family of functions instead of system() (which interposes a shell between the command and the calling process).

     If no I/O logging plugins are loaded and the policy plugin has not defined a close() function, set a command timeout or required that the command be run in a new pty, sudo may execute the command directly instead of running it as a child process.

   Plugins
     Plugins may be specified via Plugin directives in the sudo.conf(5) file.  They may be loaded as dynamic shared objects (on systems that support them), or compiled directly into the sudo binary.  If no sudo.conf(5) file is present, or it contains no Plugin
     lines, sudo will use the traditional sudoers security policy and I/O logging.  See the sudo.conf(5) manual for details of the /etc/sudo.conf file and the sudo_plugin(5) manual for more information about the sudo plugin architecture.

EXIT VALUE
     Upon successful execution of a command, the exit status from sudo will be the exit status of the program that was executed.  If the command terminated due to receipt of a signal, sudo will send itself the same signal that terminated the command.

     If the -l option was specified without a command, sudo will exit with a value of 0 if the user is allowed to run sudo and they authenticated successfully (as required by the security policy).  If a command is specified with the -l option, the exit value
     will only be 0 if the command is permitted by the security policy, otherwise it will be 1.

     If there is an authentication failure, a configuration/permission problem or if the given command cannot be executed, sudo exits with a value of 1.  In the latter case, the error string is printed to the standard error.  If sudo cannot stat(2) one or more
     entries in the user's PATH, an error is printed to the standard error.  (If the directory does not exist or if it is not really a directory, the entry is ignored and no error is printed.)  This should not happen under normal circumstances.  The most common
     reason for stat(2) to return “permission denied” is if you are running an automounter and one of the directories in your PATH is on a machine that is currently unreachable.

SECURITY NOTES
     sudo tries to be safe when executing external commands.

     To prevent command spoofing, sudo checks "." and "" (both denoting current directory) last when searching for a command in the user's PATH (if one or both are in the PATH).  Note, however, that the actual PATH environment variable is not modified and is
     passed unchanged to the program that sudo executes.

     Users should never be granted sudo privileges to execute files that are writable by the user or that reside in a directory that is writable by the user.  If the user can modify or replace the command there is no way to limit what additional commands they
     can run.

     Please note that sudo will normally only log the command it explicitly runs.  If a user runs a command such as sudo su or sudo sh, subsequent commands run from that shell are not subject to sudo's security policy.  The same is true for commands that offer
     shell escapes (including most editors).  If I/O logging is enabled, subsequent commands will have their input and/or output logged, but there will not be traditional logs for those commands.  Because of this, care must be taken when giving users access to
     commands via sudo to verify that the command does not inadvertently give the user an effective root shell.  For more information, please see the Preventing shell escapes section in sudoers(5).

     To prevent the disclosure of potentially sensitive information, sudo disables core dumps by default while it is executing (they are re-enabled for the command that is run).  This historical practice dates from a time when most operating systems allowed set-
     user-ID processes to dump core by default.  To aid in debugging sudo crashes, you may wish to re-enable core dumps by setting “disable_coredump” to false in the sudo.conf(5) file as follows:

           Set disable_coredump false

     See the sudo.conf(5) manual for more information.

ENVIRONMENT
     sudo utilizes the following environment variables.  The security policy has control over the actual content of the command's environment.

     EDITOR           Default editor to use in -e (sudoedit) mode if neither SUDO_EDITOR nor VISUAL is set.

     MAIL             Set to the mail spool of the target user when the -i option is specified or when env_reset is enabled in sudoers (unless MAIL is present in the env_keep list).

     HOME             Set to the home directory of the target user when the -i or -H options are specified, when the -s option is specified and set_home is set in sudoers, when always_set_home is enabled in sudoers, or when env_reset is enabled in sudoers and
                      HOME is not present in the env_keep list.

     LOGNAME          Set to the login name of the target user when the -i option is specified, when the set_logname option is enabled in sudoers or when the env_reset option is enabled in sudoers (unless LOGNAME is present in the env_keep list).

     PATH             May be overridden by the security policy.

     SHELL            Used to determine shell to run with -s option.

     SUDO_ASKPASS     Specifies the path to a helper program used to read the password if no terminal is available or if the -A option is specified.

     SUDO_COMMAND     Set to the command run by sudo, including command line arguments.  The command line arguments are truncated at 4096 characters to prevent a potential execution error.

     SUDO_EDITOR      Default editor to use in -e (sudoedit) mode.

     SUDO_GID         Set to the group-ID of the user who invoked sudo.

     SUDO_PROMPT      Used as the default password prompt unless the -p option was specified.

     SUDO_PS1         If set, PS1 will be set to its value for the program being run.

     SUDO_UID         Set to the user-ID of the user who invoked sudo.

     SUDO_USER        Set to the login name of the user who invoked sudo.

     USER             Set to the same value as LOGNAME, described above.

     VISUAL           Default editor to use in -e (sudoedit) mode if SUDO_EDITOR is not set.

FILES
     /etc/sudo.conf            sudo front end configuration

EXAMPLES
     Note: the following examples assume a properly configured security policy.

     To get a file listing of an unreadable directory:

           $ sudo ls /usr/local/protected

     To list the home directory of user yaz on a machine where the file system holding ~yaz is not exported as root:

           $ sudo -u yaz ls ~yaz

     To edit the index.html file as user www:

           $ sudoedit -u www ~www/htdocs/index.html

     To view system logs only accessible to root and users in the adm group:

           $ sudo -g adm more /var/log/syslog

     To run an editor as jim with a different primary group:

           $ sudoedit -u jim -g audio ~jim/sound.txt

     To shut down a machine:

           $ sudo shutdown -r +15 "quick reboot"

     To make a usage listing of the directories in the /home partition.  Note that this runs the commands in a sub-shell to make the cd and file redirection work.

           $ sudo sh -c "cd /home ; du -s * | sort -rn > USAGE"

DIAGNOSTICS
     Error messages produced by sudo include:

     editing files in a writable directory is not permitted
           By default, sudoedit does not permit editing a file when any of the parent directories are writable by the invoking user.  This avoids a race condition that could allow the user to overwrite an arbitrary file.  See the sudoedit_checkdir option in
           sudoers(5) for more information.

     editing symbolic links is not permitted
           By default, sudoedit does not follow symbolic links when opening files.  See the sudoedit_follow option in sudoers(5) for more information.

     effective uid is not 0, is sudo installed setuid root?
           sudo was not run with root privileges.  The sudo binary must be owned by the root user and have the set-user-ID bit set.  Also, it must not be located on a file system mounted with the ‘nosuid’ option or on an NFS file system that maps uid 0 to an un‐
           privileged uid.

     effective uid is not 0, is sudo on a file system with the 'nosuid' option set or an NFS file system without root privileges?
           sudo was not run with root privileges.  The sudo binary has the proper owner and permissions but it still did not run with root privileges.  The most common reason for this is that the file system the sudo binary is located on is mounted with the
           ‘nosuid’ option or it is an NFS file system that maps uid 0 to an unprivileged uid.

     fatal error, unable to load plugins
           An error occurred while loading or initializing the plugins specified in sudo.conf(5).

     invalid environment variable name
           One or more environment variable names specified via the -E option contained an equal sign (‘=’).  The arguments to the -E option should be environment variable names without an associated value.

     no password was provided
           When sudo tried to read the password, it did not receive any characters.  This may happen if no terminal is available (or the -S option is specified) and the standard input has been redirected from /dev/null.

     a terminal is required to read the password
           sudo needs to read the password but there is no mechanism available for it to do so.  A terminal is not present to read the password from, sudo has not been configured to read from the standard input, the -S option was not used, and no askpass helper
           has been specified either via the sudo.conf(5) file or the SUDO_ASKPASS environment variable.

     no writable temporary directory found
           sudoedit was unable to find a usable temporary directory in which to store its intermediate files.

     sudo must be owned by uid 0 and have the setuid bit set
           sudo was not run with root privileges.  The sudo binary does not have the correct owner or permissions.  It must be owned by the root user and have the set-user-ID bit set.

     sudoedit is not supported on this platform
           It is only possible to run sudoedit on systems that support setting the effective user-ID.

     timed out reading password
           The user did not enter a password before the password timeout (5 minutes by default) expired.

     you do not exist in the passwd database
           Your user-ID does not appear in the system passwd database.

     you may not specify environment variables in edit mode
           It is only possible to specify environment variables when running a command.  When editing a file, the editor is run with the user's environment unmodified.

SEE ALSO
     su(1), stat(2), login_cap(3), passwd(5), sudo.conf(5), sudo_plugin(5), sudoers(5), sudoers_timestamp(5), sudoreplay(8), visudo(8)

HISTORY
     See the HISTORY file in the sudo distribution (https://www.sudo.ws/history.html) for a brief history of sudo.

AUTHORS
     Many people have worked on sudo over the years; this version consists of code written primarily by:

           Todd C. Miller

     See the CONTRIBUTORS file in the sudo distribution (https://www.sudo.ws/contributors.html) for an exhaustive list of people who have contributed to sudo.

CAVEATS
     There is no easy way to prevent a user from gaining a root shell if that user is allowed to run arbitrary commands via sudo.  Also, many programs (such as editors) allow the user to run commands via shell escapes, thus avoiding sudo's checks.  However, on
     most systems it is possible to prevent shell escapes with the sudoers(5) plugin's noexec functionality.

     It is not meaningful to run the cd command directly via sudo, e.g.,

           $ sudo cd /usr/local/protected

     since when the command exits the parent process (your shell) will still be the same.  Please see the EXAMPLES section for more information.

     Running shell scripts via sudo can expose the same kernel bugs that make set-user-ID shell scripts unsafe on some operating systems (if your OS has a /dev/fd/ directory, set-user-ID shell scripts are generally safe).

BUGS
     If you feel you have found a bug in sudo, please submit a bug report at https://bugzilla.sudo.ws/

SUPPORT
     Limited free support is available via the sudo-users mailing list, see https://www.sudo.ws/mailman/listinfo/sudo-users to subscribe or search the archives.

DISCLAIMER
     sudo is provided “AS IS” and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed.  See the LICENSE file distributed with sudo or
     https://www.sudo.ws/license.html for complete details.

Sudo 1.9.1                                                                                                                    May 7, 2020                                                                                                                   Sudo 1.9.1

'''
_adduser = '''
ADDUSER(8)                                                                                                                                                                  System Manager's Manual                                                                                                                                                                  ADDUSER(8)

NAME
       adduser, addgroup - add a user or group to the system

SYNOPSIS
       adduser [options] [--home DIR] [--shell SHELL] [--no-create-home] [--uid ID] [--firstuid ID] [--lastuid ID] [--ingroup GROUP | --gid ID] [--disabled-password] [--disabled-login] [--gecos GECOS] [--add_extra_groups] user

       adduser --system [options] [--home DIR] [--shell SHELL] [--no-create-home] [--uid ID] [--group | --ingroup GROUP | --gid ID] [--disabled-password] [--disabled-login] [--gecos GECOS] user

       addgroup [options] [--gid ID] group

       addgroup --system [options] [--gid ID] group

       adduser [options] user group

   COMMON OPTIONS
       [--quiet] [--debug] [--force-badname] [--help|-h] [--version] [--conf FILE]

DESCRIPTION
       adduser  and  addgroup  add users and groups to the system according to command line options and configuration information in /etc/adduser.conf.  They are friendlier front ends to the low level tools like useradd, groupadd and usermod programs, by default choosing Debian policy conformant UID and GID values, creating a home directory with skeletal configura‐
       tion, running a custom script, and other features.  adduser and addgroup can be run in one of five modes:

   Add a normal user
       If called with one non-option argument and without the --system or --group options, adduser will add a normal user.

       adduser will choose the first available UID from the range specified for normal users in the configuration file.  The UID can be overridden with the --uid option.

       The range specified in the configuration file may be overridden with the --firstuid and --lastuid options.

       By default, each user in Debian GNU/Linux is given a corresponding group with the same name.  Usergroups allow group writable directories to be easily maintained by placing the appropriate users in the new group, setting the set-group-ID bit in the directory, and ensuring that all users use a umask of 002.  If this option is turned off by setting  USERGROUPS
       to  no, all users' GIDs are set to USERS_GID.  Users' primary groups can also be overridden from the command line with the --gid or --ingroup options to set the group by id or name, respectively.  Also, users can be added to one or more groups defined in adduser.conf either by setting ADD_EXTRA_GROUPS to 1 in adduser.conf, or by passing --add_extra_groups on
       the commandline.

       adduser will create a home directory subject to DHOME, GROUPHOMES, and LETTERHOMES.  The home directory can be overridden from the command line with the --home option, and the shell with the --shell option. The home directory's set-group-ID bit is set if USERGROUPS is yes so that any files created in the user's home directory will have the correct group.

       adduser will copy files from SKEL into the home directory and prompt for finger (gecos) information and a password.  The gecos may also be set with the --gecos option.  With the --disabled-login option, the account will be created but will be disabled until a password is set. The --disabled-password option will not set a password, but login is still possible
       (for example with SSH RSA keys).

       If the file /usr/local/sbin/adduser.local exists, it will be executed after the user account has been set up in order to do any local setup.  The arguments passed to adduser.local are:
       username uid gid home-directory
       The environment variable VERBOSE is set according to the following rule:

       0 if   --quiet is specified

       1 if neither
              --quiet nor --debug is specified

       2 if   --debug is specified

              (The same applies to the variable DEBUG, but DEBUG is deprecated and will be removed in a later version of adduser.)

   Add a system user
       If called with one non-option argument and the --system option, adduser will add a system user. If a user with the same name already exists in the system uid range (or, if the uid is specified, if a user with that uid already exists), adduser will exit with a warning. This warning can be suppressed by adding --quiet.

       adduser will choose the first available UID from the range specified for system users in the configuration file (FIRST_SYSTEM_UID and LAST_SYSTEM_UID). If you want to have a specific UID, you can specify it using the --uid option.

       By default, system users are placed in the nogroup group.  To place the new system user in an already existing group, use the --gid or --ingroup options.  To place the new system user in a new group with the same ID, use the --group option.

       A home directory is created by the same rules as for normal users.  The new system user will have the shell /usr/sbin/nologin (unless overridden with the --shell option), and have logins disabled.  Skeletal configuration files are not copied.

   Add a user group
       If adduser is called with the --group option and without the --system option, or addgroup is called respectively, a user group will be added.

       A GID will be chosen from the range specified for system GIDS in the configuration file (FIRST_GID, LAST_GID). To override that mechanism you can give the GID using the --gid option.

       The group is created with no users.

   Add a system group
       If addgroup is called with the --system option, a system group will be added.

       A GID will be chosen from the range specified for system GIDS in the configuration file (FIRST_SYSTEM_GID, LAST_SYSTEM_GID). To override that mechanism you can give the GID using the --gid option.

       The group is created with no users.

   Add an existing user to an existing group
       If called with two non-option arguments, adduser will add an existing user to an existing group.

OPTIONS
       --conf FILE
              Use FILE instead of /etc/adduser.conf.

       --disabled-login
              Do not run passwd to set the password.  The user won't be able to use her account until the password is set.

       --disabled-password
              Like --disabled-login, but logins are still possible (for example using SSH RSA keys) but not using password authentication.

       --force-badname
              By default, user and group names are checked against the configurable regular expression NAME_REGEX specified in the configuration file. This option forces adduser and addgroup to apply only a weak check for validity of the name.  NAME_REGEX is described in adduser.conf(5).

       --gecos GECOS
              Set the gecos field for the new entry generated.  adduser will not ask for finger information if this option is given.

       --gid ID
              When creating a group, this option forces the new groupid to be the given number.  When creating a user, this option will put the user in that group.

       --group
              When combined with --system, a group with the same name and ID as the system user is created.  If not combined with --system, a group with the given name is created.  This is the default action if the program is invoked as addgroup.

       --help Display brief instructions.

       --home DIR
              Use DIR as the user's home directory, rather than the default specified by the configuration file.  If the directory does not exist, it is created and skeleton files are copied.

       --shell SHELL
              Use SHELL as the user's login shell, rather than the default specified by the configuration file.

       --ingroup GROUP
              Add the new user to GROUP instead of a usergroup or the default group defined by USERS_GID in the configuration file.  This affects the users primary group.  To add additional groups, see the add_extra_groups option.

       --no-create-home
              Do not create the home directory, even if it doesn't exist.

       --quiet
              Suppress informational messages, only show warnings and errors.

       --debug
              Be verbose, most useful if you want to nail down a problem with adduser.

       --system
              Create a system user or group.

       --uid ID
              Force the new userid to be the given number.  adduser will fail if the userid is already taken.

       --firstuid ID
              Override the first uid in the range that the uid is chosen from (overrides FIRST_UID specified in the configuration file).

       --lastuid ID
              Override the last uid in the range that the uid is chosen from ( LAST_UID )

       --add_extra_groups
              Add new user to extra groups defined in the configuration file.

       --version
              Display version and copyright information.

EXIT VALUES
       0      The user exists as specified. This can have 2 causes: The user was created by adduser or the user was already present on the system before adduser was invoked. If adduser was returning 0 , invoking adduser a second time with the same parameters as before also returns 0.

       1      Creating the user or group failed because it was already present with other UID/GID than specified. The username or groupname was rejected because of a mismatch with the configured regular expressions, see adduser.conf(5). Adduser has been aborted by a signal.
              Or for many other yet undocumented reasons which are printed to console then. You may then consider to remove --quiet to make adduser more verbose.

FILES
       /etc/adduser.conf
              Default configuration file for adduser and addgroup

       /usr/local/sbin/adduser.local
              Optional custom add-ons.

SEE ALSO
       adduser.conf(5), deluser(8), groupadd(8), useradd(8), usermod(8), Debian Policy 9.2.2.

COPYRIGHT
       Copyright (C) 1997, 1998, 1999 Guy Maor. Modifications by Roland Bauerschmidt and Marc Haber. Additional patches by Joerg Hoh and Stephen Gran.
       Copyright (C) 1995 Ted Hajek, with a great deal borrowed from the original Debian adduser
       Copyright (C) 1994 Ian Murdock.  adduser is free software; see the GNU General Public Licence version 2 or later for copying conditions.  There is no warranty.

Debian GNU/Linux                                                                                                                                                                 Version 3.118                                                                                                                                                                       ADDUSER(8)

'''


