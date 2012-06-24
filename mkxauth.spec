Summary:	A utility for managing .Xauthority files
Summary(de):	Red Hat X-Autorit�ts-Utility
Summary(es):	Utilitario de Autorizaci�n X
Summary(fr):	Utilitaire Red Hat pour les permissions X
Summary(ja):	.Xauthority �ե������������뤿��Υ桼�ƥ���ƥ���
Summary(pl):	Narz�dzie do zarz�dzania plikami .Xauthority
Summary(pt_BR):	Utilit�rio de Autoriza��o X
Summary(tr):	Red Hat X yetki arac�
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
Datenbanken (.Xauthority-Dateien). Sie k�nnen eine ~/.Xauthority-Datei
erstellen oder Schl�ssel aus einer anderen lokalen oder entfernten
.Xauthority- Datei einf�gen. .Xauthority-Dateien k�nnen �ber ftp (mit
ncftp) oder rsh wiederhergestellt werden. Aus Sicherheitsgr�nden
erstellt mkxauth keine Tempor�rdateien, die
Authentifizierungsschl�ssel enthalten.

%description -l es
'mkxauth' ayuda en la creaci�n y manutenci�n de bancos de datos de
autentificaci�n X (archivos .Xauthority). �salo para crear un archivo
~/.Xauthority o para unir una llave de otro local o archivo
.Xauthority remoto. Se pueden recuperar archivos remotos .Xauthority
v�a ftp (usando ncftp) o v�a rsh. Por seguridad, mkxauth no crea
cualquier de los archivos temporales conteniendo llaves de
autentificaci�n.

%description -l fr
mkxauth aide � la cr�ation et la maintenance des bases de donn�es
d'authentification X (fichiers .Xauthority). Utilisez le pour cr�er un
fichier ~/.Xauthority ou pour fusionner des cl�s � partir d'un autre
fichier .Xauthority, local ou distant. Les fichiers .Xauthority
distants peuvent �tre obtenus via ftp (avec ncftp) ou via rsh. Pour
des raisons de s�curit�, mkxauth ne cr�e pas de fichiers temporaires
contenant les cl�s d'authentification.

%description -l ja
mkxauth �桼�ƥ���ƥ��� X ǧ�ڥǡ����١��� ( .Xauthority �ե����� )
�� ����������������ޤ���mkxauth �� .Xauthority �ե������������
������ޤ��ϥ�⡼�Ȥ� .Xauthority
�ե�����θ���������Ѥ����ޤ��� .Xauthority
�ե�����ϡ��������Ƥ˴�Ť��� X �����ФؤΥ���������
���������ݤ򤹤롢�桼���ظ��Υ�����������ȥ���ץ����Ǥ���
xauth ���Ѥ����ޤ���

X ������ɥ������ƥ�˥������ƥ����󶡤��뤿��˥桼���ظ���
������������ȥ�����Ѥ��褦�Ȥ���Τʤ顢mkxauth �ѥå�������
���󥹥ȡ��뤵���٤��Ǥ� (�����Ƥ���Ϥ褤�ͤ��Ǥ�)��

%description -l pl
Narz�dzie mkxauth pomaga tworzy� i zarz�dza� bazami danych
autentykacji X (plikami .Xauthority). mkxauth jest u�ywany do
tworzenia pliku .Xauthority oraz do��czania kluczy z innego lokalnego
lub zdalnego pliku .Xauthority. Pliki .Xauthority s� u�ywane przez
program kontroli dost�pu xauth, pozwalaj�cy lub nie na dost�p do X
serwer�w na podstawie zawarto�ci pliku .Xauthrity.

%description -l pt_BR
'mkxauth' ajuda na cria��o e manuten��o de bancos de dados de
autentica��o X (arquivos .Xauthority). Use-o para criar um arquivo
~/.Xauthority ou para unir uma chaves de outro local ou arquivo
.Xauthority remoto. Arquivos remotos .Xauthority podem ser recuperados
via ftp (usando ncftp) ou via rsh. Por seguran�a, mkxauth n�o cria
quaisquer arquivos tempor�rios contendo chaves de autentica��o.

%description -l tr
mkxauth, X yetki veritabanlar�n�n (.Xauthority dosyalar�)
olu�turulmas� ve bak�m�nda yard�mc� olur. G�venlik a��s�ndan mkxauth,
yetki anahtarlar� i�eren ge�ici dosyalar olu�turmaz.

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
