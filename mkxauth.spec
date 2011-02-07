Summary:	A utility for managing .Xauthority files
Summary(de.UTF-8):	Red Hat X-Autoritäts-Utility
Summary(es.UTF-8):	Utilitario de Autorización X
Summary(fr.UTF-8):	Utilitaire Red Hat pour les permissions X
Summary(ja.UTF-8):	.Xauthority ファイルを管理するためのユーティリティ。
Summary(pl.UTF-8):	Narzędzie do zarządzania plikami .Xauthority
Summary(pt_BR.UTF-8):	Utilitário de Autorização X
Summary(tr.UTF-8):	Red Hat X yetki aracı
Name:		mkxauth
Version:	1.7
Release:	18
License:	GPL
Group:		X11/Applications
Source0:	%{name}
Source1:	%{name}.1x
Requires:	/usr/bin/xauth
Requires:	fileutils
Requires:	gzip
Requires:	procps
Requires:	sh-utils
Requires:	textutils
BuildArch:	noarch
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

%description -l de.UTF-8
'mkxauth' hilft beim Erstellen und Verwalten von X-Authentifizierungs-
Datenbanken (.Xauthority-Dateien). Sie können eine ~/.Xauthority-Datei
erstellen oder Schlüssel aus einer anderen lokalen oder entfernten
.Xauthority- Datei einfügen. .Xauthority-Dateien können über FTP (mit
ncftp) oder rsh wiederhergestellt werden. Aus Sicherheitsgründen
erstellt mkxauth keine Temporärdateien, die
Authentifizierungsschlüssel enthalten.

%description -l es.UTF-8
'mkxauth' ayuda en la creación y manutención de bancos de datos de
autentificación X (archivos .Xauthority). Úsalo para crear un archivo
~/.Xauthority o para unir una llave de otro local o archivo
.Xauthority remoto. Se pueden recuperar archivos remotos .Xauthority
vía FTP (usando ncftp) o vía rsh. Por seguridad, mkxauth no crea
cualquier de los archivos temporales conteniendo llaves de
autentificación.

%description -l fr.UTF-8
mkxauth aide à la création et la maintenance des bases de données
d'authentification X (fichiers .Xauthority). Utilisez le pour créer un
fichier ~/.Xauthority ou pour fusionner des clés à partir d'un autre
fichier .Xauthority, local ou distant. Les fichiers .Xauthority
distants peuvent être obtenus via FTP (avec ncftp) ou via rsh. Pour
des raisons de sécurité, mkxauth ne crée pas de fichiers temporaires
contenant les clés d'authentification.

%description -l ja.UTF-8
mkxauth ユーティリティは X 認証データベース ( .Xauthority ファイル )
の 生成と整備を助けます。mkxauth は .Xauthority ファイルの生成、
ローカルまたはリモートの .Xauthority
ファイルの鍵の統合に用いられます。 .Xauthority
ファイルは、その内容に基づいて X サーバへのアクセスの
承諾、拒否をする、ユーザ指向のアクセスコントロールプログラムである
xauth に用いられます。

X ウィンドウシステムにセキュリティを提供するためにユーザ指向の
アクセスコントロールを用いようとするのなら、mkxauth パッケージは
インストールされるべきです (そしてそれはよい考えです)。

%description -l pl.UTF-8
Narzędzie mkxauth pomaga tworzyć i zarządzać bazami danych
autentykacji X (plikami .Xauthority). mkxauth jest używany do
tworzenia pliku .Xauthority oraz dołączania kluczy z innego lokalnego
lub zdalnego pliku .Xauthority. Pliki .Xauthority są używane przez
program kontroli dostępu xauth, pozwalający lub nie na dostęp do X
serwerów na podstawie zawartości pliku .Xauthrity.

%description -l pt_BR.UTF-8
'mkxauth' ajuda na criação e manutenção de bancos de dados de
autenticação X (arquivos .Xauthority). Use-o para criar um arquivo
~/.Xauthority ou para unir uma chaves de outro local ou arquivo
.Xauthority remoto. Arquivos remotos .Xauthority podem ser recuperados
via FTP (usando ncftp) ou via rsh. Por segurança, mkxauth não cria
quaisquer arquivos temporários contendo chaves de autenticação.

%description -l tr.UTF-8
mkxauth, X yetki veritabanlarının (.Xauthority dosyaları)
oluşturulması ve bakımında yardımcı olur. Güvenlik açısından mkxauth,
yetki anahtarları içeren geçici dosyalar oluşturmaz.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/mkxauth
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/mkxauth.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkxauth
%{_mandir}/man1/mkxauth*
