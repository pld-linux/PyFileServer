#
# TODO:
# - check if PyXML is really required during build
#
Summary:	A WebDAV server in Python
Summary(pl):	Serwer WebDAV napisany w Pythonie
Name:		PyFileServer
Version:	0.2.1
Release:	0.1
License:	BSD
Group:		Networking/Daemons
Source0:	http://download.berlios.de/pyfilesync/PyFileServer-0.2.1.zip
# Source0-md5:	7a46d3f94e05d81b4110e6d0780c642b
URL:		http://pyfilesync.berlios.de/pyfileserver.html
BuildRequires:	python >= 2.3
BuildRequires:	unzip
%pyrequires_eq	python-modules
Requires:	python-PyXML
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyFileServer implements up to Class 2 of the WebDAV specification,
including support for shared and exclusive write locking, and setting
arbitrary dead properties. It also implements HTTP user authentication
using both basic and digest schemes, HTTP single range retrievals and
conditional processing headers (If_Match, If_Modified_Since, etc).

PyFileServer also allows custom components to be developed easily by
having clear interfaces for:
 - Resource Abstraction Layer
 - Lock Manager
 - Property Manager
 - Domain Controllers

%description -l pl
PyFileSerwer implementuje specyfikacjê WebDAV do klasy 2 w³±cznie,
wraz z obs³ug± wspó³dzielonych i wy³±cznych blokad zapisu oraz
ustawianiem dowolnych martwych w³asno¶ci. Implementuje tak¿e
uwierzytelnianie u¿ytkowników po HTTP przy u¿yciu schematów basic i
digest, pojedyncze zakresy ¶ci±gania danych po HTTP oraz nag³ówki
przetwarzania warunkowego (If_Match, If_Modified_Since itp.).

PyFileServer pozwala tak¿e na ³atwe tworzenie w³asnych komponentów
udostêpniaj±c przejrzyste interfejsy do:
 - warstwy abstrakcji zasobów (Resource Abstraction Layer)
 - zarz±dcy blokad (Lock Manager)
 - zarz±dcy w³asno¶ci (Property Manager)
 - kontrolerów domen (Domain Controllers)

%prep
%setup -q -n %{name}

%build
%py_comp pyfileserver/
%py_ocomp pyfileserver/

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

cp -r pyfileserver $RPM_BUILD_ROOT%{py_sitescriptdir}
echo "#!/usr/bin/python" > $RPM_BUILD_ROOT%{_bindir}/PyFileServer.py
cat ext_wsgiutils_server.py >> $RPM_BUILD_ROOT%{_bindir}/PyFileServer.py

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ADDONS.txt DEVELOPERS.txt PyFileServer-example.conf README.txt 
%doc THANKS.txt TODO.txt TUTORIAL.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/pyfileserver
