#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-trtf
Version  : 0.3.8
Release  : 3
URL      : https://cran.r-project.org/src/contrib/trtf_0.3-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/trtf_0.3-8.tar.gz
Summary  : Transformation Trees and Forests
Group    : Development/Tools
License  : GPL-2.0
Requires: R-Formula
Requires: R-libcoin
Requires: R-mlt
Requires: R-partykit
Requires: R-sandwich
Requires: R-variables
BuildRequires : R-Formula
BuildRequires : R-TH.data
BuildRequires : R-alabama
BuildRequires : R-basefun
BuildRequires : R-coin
BuildRequires : R-coneproj
BuildRequires : R-libcoin
BuildRequires : R-mlt
BuildRequires : R-partykit
BuildRequires : R-sandwich
BuildRequires : R-variables
BuildRequires : buildreq-R

%description
corresponding random forest for conditional transformation models

%prep
%setup -q -c -n trtf
cd %{_builddir}/trtf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641141065

%install
export SOURCE_DATE_EPOCH=1641141065
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library trtf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library trtf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library trtf
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc trtf || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/trtf/BMI_artificial.rda
/usr/lib64/R/library/trtf/DESCRIPTION
/usr/lib64/R/library/trtf/INDEX
/usr/lib64/R/library/trtf/Meta/Rd.rds
/usr/lib64/R/library/trtf/Meta/demo.rds
/usr/lib64/R/library/trtf/Meta/features.rds
/usr/lib64/R/library/trtf/Meta/hsearch.rds
/usr/lib64/R/library/trtf/Meta/links.rds
/usr/lib64/R/library/trtf/Meta/nsInfo.rds
/usr/lib64/R/library/trtf/Meta/package.rds
/usr/lib64/R/library/trtf/NAMESPACE
/usr/lib64/R/library/trtf/NEWS.Rd
/usr/lib64/R/library/trtf/R/trtf
/usr/lib64/R/library/trtf/R/trtf.rdb
/usr/lib64/R/library/trtf/R/trtf.rdx
/usr/lib64/R/library/trtf/demo/BMI.R
/usr/lib64/R/library/trtf/demo/QRF.R
/usr/lib64/R/library/trtf/demo/applications.R
/usr/lib64/R/library/trtf/help/AnIndex
/usr/lib64/R/library/trtf/help/aliases.rds
/usr/lib64/R/library/trtf/help/paths.rds
/usr/lib64/R/library/trtf/help/trtf.rdb
/usr/lib64/R/library/trtf/help/trtf.rdx
/usr/lib64/R/library/trtf/html/00Index.html
/usr/lib64/R/library/trtf/html/R.css
/usr/lib64/R/library/trtf/ordinal_forests/ALS/01_ALS_sample.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/02_run_1_100.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/02_run_1_120.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/03_summary_plots.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/ALS_analysis.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/ALS_competitors.R
/usr/lib64/R/library/trtf/ordinal_forests/ALS/README.txt
/usr/lib64/R/library/trtf/ordinal_forests/README.txt
/usr/lib64/R/library/trtf/ordinal_forests/empeval/01_data_simulation.R
/usr/lib64/R/library/trtf/ordinal_forests/empeval/02_empeval.R
/usr/lib64/R/library/trtf/ordinal_forests/empeval/03_summary_plots.R
/usr/lib64/R/library/trtf/ordinal_forests/empeval/README.txt
/usr/lib64/R/library/trtf/ordinal_forests/empeval/competitors.R
/usr/lib64/R/library/trtf/sim/2d.R
/usr/lib64/R/library/trtf/sim/README.txt
/usr/lib64/R/library/trtf/sim/artificial_simfun.R
/usr/lib64/R/library/trtf/sim/friedman.R
/usr/lib64/R/library/trtf/sim/lognormal_2d.R
/usr/lib64/R/library/trtf/sim/lognormal_friedman.R
/usr/lib64/R/library/trtf/sim/plots.R
/usr/lib64/R/library/trtf/sim/runsim.R
/usr/lib64/R/library/trtf/sim/summary.R
/usr/lib64/R/library/trtf/sim/timings.R
/usr/lib64/R/library/trtf/sim/timings_nmax.R
/usr/lib64/R/library/trtf/survival_forests/ALS/ALS_supplement.R
/usr/lib64/R/library/trtf/survival_forests/README.txt
/usr/lib64/R/library/trtf/survival_forests/predictive/README.txt
/usr/lib64/R/library/trtf/survival_forests/predictive/tr_competitors.R
/usr/lib64/R/library/trtf/survival_forests/predictive/tr_data_simulation.R
/usr/lib64/R/library/trtf/survival_forests/predictive/tr_empeval.R
/usr/lib64/R/library/trtf/survival_forests/predictive/tr_empeval_plot.R
/usr/lib64/R/library/trtf/survival_forests/predictive/tr_results_empeval.rda
/usr/lib64/R/library/trtf/survival_forests/prognostic/README.txt
/usr/lib64/R/library/trtf/survival_forests/prognostic/competitors.R
/usr/lib64/R/library/trtf/survival_forests/prognostic/data_simulation.R
/usr/lib64/R/library/trtf/survival_forests/prognostic/empeval.R
/usr/lib64/R/library/trtf/survival_forests/prognostic/empeval_plot.R
/usr/lib64/R/library/trtf/survival_forests/prognostic/results_empeval.rda
/usr/lib64/R/library/trtf/survival_forests/prognostic/summary.R
/usr/lib64/R/library/trtf/tests/GBSG2-Ex.R
/usr/lib64/R/library/trtf/tests/regtest-traforest.R
/usr/lib64/R/library/trtf/tests/regtest-trafotree.R
