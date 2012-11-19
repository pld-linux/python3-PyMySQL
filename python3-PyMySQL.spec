%define	snap	20121119
%define	rel	1
Summary:	Pure Python 3 MySQL Client
Name:		python3-PyMySQL
Version:	0.6
Release:	0.%{snap}.%{rel}
License:	MIT
Group:		Libraries/Python
#Source0:	https://github.com/downloads/petehunt/PyMySQL/PyMySQL3-%{version}.tar.gz
Source0:	https://github.com/petehunt/PyMySQL/tarball/master/%{name}-%{version}.tar.gz
# Source0-md5:	8bb32225d3590dd56ec586f4d125edbd
URL:		http://www.pymysql.org/
BuildRequires:	python3-2to3
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a pure-Python 3 MySQL client library.

The goal of pymysql is to be a drop-in replacement for MySQLdb and
work on CPython 2.3+, Jython, IronPython, PyPy and Python 3.

%prep
#%%setup  -q -n PyMySQL3-%{version}
%setup -q -n petehunt-PyMySQL-bd9c588
sed -i -e 's#2to3#2to3-3.2#g' build-py3k.sh

%build
sh ./build-py3k.sh
cd py3k
PYTHONPATH=$(pwd)/pymysql %{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
cd py3k
python3 -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/PyMySQL3-*.egg-info
%{py3_sitescriptdir}/pymysql
