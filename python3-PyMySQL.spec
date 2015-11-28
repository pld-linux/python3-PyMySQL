Summary:	Pure Python 3 MySQL Client
Name:		python3-PyMySQL
Version:	0.6.2
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/PyMySQL/PyMySQL/archive/pymysql-%{version}.tar.gz
# Source0-md5:	d16b0b4b1fe5a5c397525da4bc8a3e46
URL:		http://www.pymysql.org/
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a pure-Python 3 MySQL client library.

The goal of pymysql is to be a drop-in replacement for MySQLdb and
work on CPython 2.3+, Jython, IronPython, PyPy and Python 3.

%prep
%setup  -q -n PyMySQL-pymysql-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/PyMySQL-%{version}-py*.egg-info
%{py3_sitescriptdir}/pymysql
