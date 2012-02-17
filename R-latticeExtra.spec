%bcond_without bootstrap
%global packname  latticeExtra
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.6_19
Release:          1
Summary:          Extra Graphical Utilities Based on Lattice
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-19.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-RColorBrewer R-lattice 
Requires:         R-lattice R-grid 
%if %{with bootstrap}
%else
Requires:         R-maps R-mapproj R-deldir R-tripack R-quantreg R-zoo R-MASS R-mgcv 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-RColorBrewer R-lattice
BuildRequires:    R-lattice R-grid 
%if %{with bootstrap}
%else
BuildRequires:    R-maps R-mapproj R-deldir R-tripack R-quantreg R-zoo R-MASS R-mgcv 
%endif

%description
Extra graphical utilities based on lattice

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/scripts
