Summary:	A utility for managing .Xauthority files
Summary(de):	Red Hat X-Autoritäts-Utility
Summary(es):	Utilitario de Autorización X
Summary(fr):	Utilitaire Red Hat pour les permissions X
Summary(ja):	.Xauthority ¥Õ¥¡¥¤¥ë¤ò´ÉÍý¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡£
Summary(pl):	Narzêdzie do zarz±dzania plikami .Xauthority
Summary(pt_BR):	Utilitário de Autorização X
Summary(tr):	Red Hat X yetki aracý
Name:		mkxauth
Version:	1.7
Release:	17
License:	GPL
Group:		X11/Applications
Source0:	%{name}
Source1:	%{name}.1x
BuildArch:	noarch
Requires:	/usr/X11R6/bin/xauth
Requires:	fileutils
Requires:	gzip
Requires:	procps
Requires:	sh-utils
Requires:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l de

kxauth' hilft beim Erstellen und Verwalten von X-Authentifizierungs-
Datenbanken (.Xauthority-Dateien). Sie können eine ~/.Xauthority-Datei
erstellen oder Schlüssel aus einer anderen lokalen oder entfernten
.Xauthority- Datei einfügen. .Xauthority-Dateien können über ftp (mit
ncftp) oder rsh wiederhergestellt werden. Aus Sicherheitsgründen
erstellt mkxauth keine Temporärdateien, die
Authentifizierungsschlüssel enthalten.

%description -l es
'mkxauth' ayuda en la creación y manutención de bancos de datos de
autentificación X (archivos .Xauthority). Úsalo para crear un archivo
~/.Xauthority o para unir una llave de otro local o archivo
.Xauthority remoto. Se pueden recuperar archivos remotos .Xauthority
vía ftp (usando ncftp) o vía rsh. Por seguridad, mkxauth no crea
cualquier de los archivos temporales conteniendo llaves de
autentificación.

%description -l fr
mkxauth aide à la création et la maintenance des bases de données
d'authentification X (fichiers .Xauthority). Utilisez le pour créer un
fichier ~/.Xauthority ou pour fusionner des clés à partir d'un autre
fichier .Xauthority, local ou distant. Les fichiers .Xauthority
distants peuvent être obtenus via ftp (avec ncftp) ou via rsh. Pour
des raisons de sécurité, mkxauth ne crée pas de fichiers temporaires
contenant les clés d'authentification.

%description -l ja
mkxauth ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï X Ç§¾Ú¥Ç¡¼¥¿¥Ù¡¼¥¹ ( .Xauthority ¥Õ¥¡¥¤¥ë )
¤Î À¸À®¤ÈÀ°È÷¤ò½õ¤±¤Þ¤¹¡£mkxauth ¤Ï .Xauthority ¥Õ¥¡¥¤¥ë¤ÎÀ¸À®¡¢
¥í¡¼¥«¥ë¤Þ¤¿¤Ï¥ê¥â¡¼¥È¤Î .Xauthority
¥Õ¥¡¥¤¥ë¤Î¸°¤ÎÅý¹ç¤ËÍÑ¤¤¤é¤ì¤Þ¤¹¡£ .Xauthority
¥Õ¥¡¥¤¥ë¤Ï¡¢¤½¤ÎÆâÍÆ¤Ë´ð¤Å¤¤¤Æ X ¥µ¡¼¥Ð¤Ø¤Î¥¢¥¯¥»¥¹¤Î
¾µÂú¡¢µñÈÝ¤ò¤¹¤ë¡¢¥æ¡¼¥¶»Ø¸þ¤Î¥¢¥¯¥»¥¹¥³¥ó¥È¥í¡¼¥ë¥×¥í¥°¥é¥à¤Ç¤¢¤ë
xauth ¤ËÍÑ¤¤¤é¤ì¤Þ¤¹¡£

X ¥¦¥£¥ó¥É¥¦¥·¥¹¥Æ¥à¤Ë¥»¥­¥å¥ê¥Æ¥£¤òÄó¶¡¤¹¤ë¤¿¤á¤Ë¥æ¡¼¥¶»Ø¸þ¤Î
¥¢¥¯¥»¥¹¥³¥ó¥È¥í¡¼¥ë¤òÍÑ¤¤¤è¤¦¤È¤¹¤ë¤Î¤Ê¤é¡¢mkxauth ¥Ñ¥Ã¥±¡¼¥¸¤Ï
¥¤¥ó¥¹¥È¡¼¥ë¤µ¤ì¤ë¤Ù¤­¤Ç¤¹ (¤½¤·¤Æ¤½¤ì¤Ï¤è¤¤¹Í¤¨¤Ç¤¹)¡£

%description -l pl
Narzêdzie mkxauth pomaga tworzyæ i zarz±dzaæ bazami danych
autentykacji X (plikami .Xauthority). mkxauth jest u¿ywany do
tworzenia pliku .Xauthority oraz do³±czania kluczy z innego lokalnego
lub zdalnego pliku .Xauthority. Pliki .Xauthority s± u¿ywane przez
program kontroli dostêpu xauth, pozwalaj±cy lub nie na dostêp do X
serwerów na podstawie zawarto¶ci pliku .Xauthrity.

%description -l pt_BR
'mkxauth' ajuda na criação e manutenção de bancos de dados de
autenticação X (arquivos .Xauthority). Use-o para criar um arquivo
~/.Xauthority ou para unir uma chaves de outro local ou arquivo
.Xauthority remoto. Arquivos remotos .Xauthority podem ser recuperados
via ftp (usando ncftp) ou via rsh. Por segurança, mkxauth não cria
quaisquer arquivos temporários contendo chaves de autenticação.

%description -l tr
mkxauth, X yetki veritabanlarýnýn (.Xauthority dosyalarý)
oluþturulmasý ve bakýmýnda yardýmcý olur. Güvenlik açýsýndan mkxauth,
yetki anahtarlarý içeren geçici dosyalar oluþturmaz.

%prep

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
