#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Mail
%define		pnam	SpamTest-Bayesian
Summary:	Mail::SpamTest::Bayesian - Perl extension for Bayesian spam-testing
Summary(pl.UTF-8):	Mail::SpamTest::Bayesian - rozszerzenie Perla do wykrywania spamu metodą bayesowską
Name:		perl-Mail-SpamTest-Bayesian
Version:	0.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3656a57490c6ff342ba180da3ec9762
URL:		http://search.cpan.org/dist/Mail-SpamTest-Bayesian/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(MIME::Parser) >= 5.406
BuildRequires:	perl-BerkeleyDB >= 0.17
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the Bayesian spam-testing algorithm described
by Paul Graham at <http://www.paulgraham.com/spam.html>.

In short: the system is trained by exposure to mailboxes of known spam
and non-spam messages. These are (1) MIME-decoded, and non-text parts
deleted; (2) tokenised. The database files spam.db and nonspam.db
contain lists of tokens and the number of messages in which they have
occurred; general.db holds a message count.

%description -l pl.UTF-8
Ten moduł jest implementacją bayesowskiego algorytmu wykrywania spamu
opisanego przez Paula Grahama w <http://www.paulgraham.com/spam.html>.

W skrócie: system jest uczony poprzez przedstawianie skrzynek z
wiadomościami, o których wiadomo, że zawierają spam lub go nie
zawierają. Są one (1) zakodowane MIME, z usuniętymi częściami
nietekstowymi; (2) ztokenizowane. Pliki baz danych spam.db i
nonspam.db zawierają listy tokenów i liczby wiadomości, w których
wystąpiły; general.db przechowuje liczbę wiadomości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_vendorlib}/Mail/SpamTest
%{perl_vendorlib}/Mail/SpamTest/*.pm
%{_mandir}/man3/*
