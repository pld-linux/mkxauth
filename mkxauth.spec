Summary:	A utility for managing .Xauthority files
Summary(pl):	Narzêdzie do zarz±dzania plikami .Xauthority
Name:		mkxauth
Version:	1.7
Release:	11
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	%{name}
Source1:	%{name}.1x
BuildArch:	noarch
Requires:	/usr/X11R6/bin/xauth textutils fileutils sh-utils procps gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The mkxauth utility helps create and maintain X authentication
databases (.Xauthority files). Mkxauth is used to create an
.Xauthority file or to merge keys from another local or remote
.Xauthority file. .Xauthority files are used by the xauth
user-oriented access control program, which grants or denies access to
X servers based on the contents of the .Xauthority file.

The mkxauth package should be installed if you're going to use
user-oriented access control to provide security for your X Window
System (a good idea).

%description -l pl
Narzêdzie mkxauth pomaga tworzyæ i zarz±dzaæ bazami danych
autentykacji X (plikami .Xauthority). mkxauth jest u¿ywany do
tworzenia pliku .Xauthority oraz do³±czania kluczy z innego lokalnego
lub zdalnego pliku .Xauthority. Pliki .Xauthority s± u¿ywane przez
program kontroli dostêpu xauth, pozwalaj±cy lub nie na dostêp do X
serwerów na podstawie zawarto¶ci pliku .Xauthrity.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,man/man1}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/mkxauth
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/mkxauth.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkxauth
%{_mandir}/man1/mkxauth*
