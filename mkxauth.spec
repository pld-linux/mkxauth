Summary: A utility for managing .Xauthority files.
Name: mkxauth
Version: 1.7
Release: 11
Copyright: GPL
Group: Applications/System
Source0: mkxauth
Source1: mkxauth.1x
BuildArchitectures: noarch
Requires: /usr/X11R6/bin/xauth textutils fileutils sh-utils procps gzip
Prefix: /usr/X11R6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkxauth utility helps create and maintain X authentication
databases (.Xauthority files).  Mkxauth is used to create an
.Xauthority file or to merge keys from another local or remote
.Xauthority file.  .Xauthority files are used by the xauth
user-oriented access control program, which grants or denies
access to X servers based on the contents of the .Xauthority
file.

The mkxauth package should be installed if you're going to use
user-oriented access control to provide security for your X Window
System (a good idea).

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

install -m 0755 $RPM_SOURCE_DIR/mkxauth $RPM_BUILD_ROOT/usr/X11R6/bin/mkxauth
install -m 0444 $RPM_SOURCE_DIR/mkxauth.1x $RPM_BUILD_ROOT/usr/X11R6/man/man1/mkxauth.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/mkxauth
/usr/X11R6/man/man1/mkxauth*
