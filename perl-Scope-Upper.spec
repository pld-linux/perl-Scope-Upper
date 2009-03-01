#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Scope
%define	pnam	Upper
Summary:	Scope::Upper - Act on upper scopes.
#Summary(pl.UTF-8):	
Name:		perl-Scope-Upper
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Scope/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9fcfab05a267376fa3f560f310ab16ce
URL:		http://search.cpan.org/dist/Scope-Upper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you defer actions at run-time that will take place
when the control flow returns into an upper scope.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorarch}/Scope
%dir %{perl_vendorarch}/auto/Scope
%{perl_vendorarch}/Scope/*.pm
%dir %{perl_vendorarch}/auto/Scope/Upper
%{perl_vendorarch}/auto/Scope/Upper/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Scope/Upper/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
