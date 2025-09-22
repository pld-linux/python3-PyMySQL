%bcond_with	tests
Summary:	Pure Python 3 MySQL Client
Name:		python3-PyMySQL
Version:	1.1.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/PyMySQL/PyMySQL/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	4d08f0939106f2eb1d01ae5878e5e7f6
URL:		https://github.com/PyMySQL/PyMySQL/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a pure-Python 3 MySQL client library.

The goal of pymysql is to be a drop-in replacement for MySQLdb and
work on CPython 2.3+, Jython, IronPython, PyPy and Python 3.

%prep
%setup  -q -n PyMySQL-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md SECURITY.md
%{py3_sitescriptdir}/pymysql-%{version}.dist-info
%{py3_sitescriptdir}/pymysql
