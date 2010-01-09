%define upstream_name    HTML-FormFu
%define upstream_version 0.06001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Strip shitespace from HTML output
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI)
BuildRequires: perl(Captcha::reCAPTCHA)
BuildRequires: perl(Class::Accessor::Chained::Fast)
BuildRequires: perl(Class::C3)
BuildRequires: perl(Class::Factory::Util)
BuildRequires: perl(Config::Any)
BuildRequires: perl(Crypt::CBC)
BuildRequires: perl(Crypt::DES)
BuildRequires: perl(Data::Visitor)
BuildRequires: perl(Data::Visitor::Callback)
BuildRequires: perl(Date::Calc)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)
BuildRequires: perl(DateTime::Format::Natural)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(DateTime::Locale)
BuildRequires: perl(Email::Valid)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(HTML::Scrubber)
BuildRequires: perl(HTML::TokeParser::Simple)
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(Hash::Flatten)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Locale::Maketext)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Number::Format)
BuildRequires: perl(Path::Class::File)
BuildRequires: perl(Readonly)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Regexp::Copy)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(YAML::XS)
BuildRequires: perl(boolean)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Regexp::Copy)

%description
the HTML::FormFu manpage is a HTML form framework which aims to be as easy
as possible to use for basic web forms, but with the power and flexibility
to do anything else you might want to do (as long as it involves forms).

You can configure almost any part of formfu's behaviour and output. By
default formfu renders "XHTML 1.0 Strict" compliant markup, with as little
extra markup as possible, but with sufficient CSS class names to allow for
a wide-range of output styles to be generated by changing only the CSS.

All methods listed below (except the /new manpage) can either be called as
a normal method on your '$form' object, or as an option in your config
file. Examples will mainly be shown in the YAML manpage config syntax.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/html_formfu_deploy.pl
/usr/bin/html_formfu_dumpconf.pl
/usr/share/man/man1/html_formfu_deploy.pl.1.lzma
/usr/share/man/man1/html_formfu_dumpconf.pl.1.lzma
