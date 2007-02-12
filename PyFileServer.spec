Summary:	A WebDAV server in Python
Summary(pl.UTF-8):   Serwer WebDAV napisany w Pythonie
Name:		PyFileServer
Version:	0.2.1
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://download.berlios.de/pyfilesync/PyFileServer-0.2.1.zip
# Source0-md5:	7a46d3f94e05d81b4110e6d0780c642b
URL:		http://pyfilesync.berlios.de/pyfileserver.html
Patch0:		%{name}-setup_py.patch
BuildRequires:	python >= 2.3
BuildRequires:	python-setuptools
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

%description -l pl.UTF-8
PyFileSerwer implementuje specyfikację WebDAV do klasy 2 włącznie,
wraz z obsługą współdzielonych i wyłącznych blokad zapisu oraz
ustawianiem dowolnych martwych własności. Implementuje także
uwierzytelnianie użytkowników po HTTP przy użyciu schematów basic i
digest, pojedyncze zakresy ściągania danych po HTTP oraz nagłówki
przetwarzania warunkowego (If_Match, If_Modified_Since itp.).

PyFileServer pozwala także na łatwe tworzenie własnych komponentów
udostępniając przejrzyste interfejsy do:
 - warstwy abstrakcji zasobów (Resource Abstraction Layer)
 - zarządcy blokad (Lock Manager)
 - zarządcy własności (Property Manager)
 - kontrolerów domen (Domain Controllers)

%prep
%setup -q -n %{name}
%patch0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT



install -d $RPM_BUILD_ROOT%{_bindir}
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
%{py_sitescriptdir}/PyFileServer*
