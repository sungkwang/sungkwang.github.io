import re

with open('publications.html', 'r', encoding='utf-8') as f:
    content = f.read()

journals_old_html = """            <li> A. Bakhtiarydavijani, M. Murphy, Sungkwang Mun, M. Jones, D. Bammann, M. LaPlaca, M. Horstemeyer, and R. Prabhu, <em>"Damage biomechanics for neuronal membrane mechanoporation"</em>, Modelling and Simulation in Materials Science and Engineering, vol. 27, no. 6, pp. 065004, 2019.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1088/1361-651x/ab1efe" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Bakhtiarydavijani2019')">BibTeX</button>]
                </div>
                <div id="Bakhtiarydavijani2019" class="bibtex-block">@article{Bakhtiarydavijani2019,
  author = {A. Bakhtiarydavijani and M. Murphy and Sungkwang Mun and M. Jones and D. Bammann and M. LaPlaca and M. Horstemeyer and R. Prabhu},
  title = {Damage biomechanics for neuronal membrane mechanoporation},
  journal = {Modelling and Simulation in Materials Science and Engineering},
  year = {2019},
  volume = {27},
  number = {6},
  pages = {065004}
}</div>
            </li>
            <li> A. L. Bowman, Sungkwang Mun, S. R. Gwaltney, M. I. Baskes, and M. F. Horstemeyer, <em>"Free volume and structural evolution during creep in amorphous polyethylene by atomistic molecular dynamic simulations"</em>, Polymer, vol. 170, pp. 85–100, 2019.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1016/j.polymer.2019.02.060" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Bowman2019')">BibTeX</button>]
                </div>
                <div id="Bowman2019" class="bibtex-block">@article{Bowman2019,
  author = {A. L. Bowman and Sungkwang Mun and S. R. Gwaltney and M. I. Baskes and M. F. Horstemeyer},
  title = {Free volume and structural evolution during creep in amorphous polyethylene by atomistic molecular dynamic simulations},
  journal = {Polymer},
  year = {2019},
  volume = {170},
  pages = {85-100}
}</div>
            </li>
            <li> D. Dickel, S. R. Gwaltney, Sungkwang Mun, M. I. Baskes, and M. F. Horstemeyer, <em>"A dispersion-corrected modified embedded-atom method bond order interatomic potential for sulfur"</em>, The Journal of Physical Chemistry A, 2018.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1021/acs.jpca.8b07410" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Dickel2018')">BibTeX</button>]
                </div>
                <div id="Dickel2018" class="bibtex-block">@article{Dickel2018,
  author = {D. Dickel and S. R. Gwaltney and Sungkwang Mun and M. I. Baskes and M. F. Horstemeyer},
  title = {A dispersion-corrected modified embedded-atom method bond order interatomic potential for sulfur},
  journal = {The Journal of Physical Chemistry A},
  year = {2018}
}</div>
            </li>
            <li> M. A. Murphy, Sungkwang Mun, M. F. Horstemeyer, M. I. Baskes, A. Bakhtiary, Michelle C. LaPlaca, Steven R. Gwaltney, Lakiesha N. Williams, and R. K. Prabhu, <em>"Molecular dynamics simulations showing 1-palmitoyl-2-oleoyl-phosphatidylcholine (POPC) membrane mechanoporation damage under different strain paths"</em>, Journal of Biomolecular Structure and Dynamics, vol. 0, no. 0, pp. 1–14, 2018.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1080/07391102.2018.1453376" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Murphy2018')">BibTeX</button>]
                </div>
                <div id="Murphy2018" class="bibtex-block">@article{Murphy2018,
  author = {M. A. Murphy and Sungkwang Mun and M. F. Horstemeyer and M. I. Baskes and A. Bakhtiary and Michelle C. LaPlaca and Steven R. Gwaltney and Lakiesha N. Williams and R. K. Prabhu},
  title = {Molecular dynamics simulations showing 1-palmitoyl-2-oleoyl-phosphatidylcholine (POPC) membrane mechanoporation damage under different strain paths},
  journal = {Journal of Biomolecular Structure and Dynamics},
  year = {2018},
  volume = {0},
  number = {0},
  pages = {1-14}
}</div>
            </li>
            <li> Nayeon Lee, Lakiesha N. Williams, Sungkwang Mun, R. Prabhu, Kabindra R. Bhattarai, H. Rhee, and M.F. Horstemeyer, <em>"Stress wave mitigation at suture interfaces"</em>, Biomedical Physics &amp; Engineering Express, vol. 3, no. 3, pp. 035025, 2017.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1088/2057-1976/aa777e" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Lee2017')">BibTeX</button>]
                </div>
                <div id="Lee2017" class="bibtex-block">@article{Lee2017,
  author = {Nayeon Lee and Lakiesha N. Williams and Sungkwang Mun and R. Prabhu and Kabindra R. Bhattarai and H. Rhee and M.F. Horstemeyer},
  title = {Stress wave mitigation at suture interfaces},
  journal = {Biomedical Physics & Engineering Express},
  year = {2017},
  volume = {3},
  number = {3},
  pages = {035025}
}</div>
            </li>
            <li> Sungkwang Mun, Andrew L. Bowman, Sasan Nouranian, Steven R. Gwaltney, Michael I. Baskes, and Mark F. Horstemeyer, <em>"Interatomic potential for hydrocarbons on the basis of the modified embedded-atom method with bond order (MEAM-BO)"</em>, The Journal of Physical Chemistry A, vol. 121, no. 7, pp. 1502–1524, 2017.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1021/acs.jpca.6b11343" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Mun2017')">BibTeX</button>]
                </div>
                <div id="Mun2017" class="bibtex-block">@article{Mun2017,
  author = {Sungkwang Mun and Andrew L. Bowman and Sasan Nouranian and Steven R. Gwaltney and Michael I. Baskes and Mark F. Horstemeyer},
  title = {Interatomic potential for hydrocarbons on the basis of the modified embedded-atom method with bond order (MEAM-BO)},
  journal = {The Journal of Physical Chemistry A},
  year = {2017},
  volume = {121},
  number = {7},
  pages = {1502-1524}
}</div>
            </li>
            <li> Sungkwang Mun, G. F. Sassenrath, A. M. Schmidt, Nayeon Lee, M. C. Wadsworth, B. Rice, J.Q. Corbitt, J. Pote, and R. Prabhu, <em>"Uncertainty analysis of an irrigation scheduling model for water management in crop production"</em>, Agricultural Water Management, vol. 155, pp. 100–112, 2015.
                <div class="pub-actions">
                    [<a href="https://doi.org/10.1016/j.agwat.2015.03.009" target="_blank">Publisher</a>]
                    [<button type="button" onclick="toggleBibtex('Mun2015')">BibTeX</button>]
                </div>
                <div id="Mun2015" class="bibtex-block">@article{Mun2015,
  author = {Sungkwang Mun and G. F. Sassenrath and A. M. Schmidt and Nayeon Lee and M. C. Wadsworth and B. Rice and J.Q. Corbitt and J. Pote and R. Prabhu},
  title = {Uncertainty analysis of an irrigation scheduling model for water management in crop production},
  journal = {Agricultural Water Management},
  year = {2015},
  volume = {155},
  pages = {100-112}
}</div>
            </li>
"""

# Insert journals right before the FMT2012 paper
content = content.replace('            <li> J. E. Fowler, S. Mun and E. W. Tramel, <em>"Block-Based Compressed Sensing of Images and Video"</em>', journals_old_html + '            <li> J. E. Fowler, S. Mun and E. W. Tramel, <em>"Block-Based Compressed Sensing of Images and Video"</em>')

software_and_pres_html = """
        <h3>Software Manuals</h3>
        <ol class="pub-list">
            <li> Sungkwang Mun, S. Adibi, D. Dickel, and L. Bian, <em>"PINN for Predicting the Thermal Evolution of WAAM Proces"</em>, Army Research Lab, 2020. Software User Manual.
            </li>
        </ol>

        <h3>Conference Presentations</h3>
        <ol class="pub-list">
            <li> Sungkwang Mun, R. Carino, and M. Baskes, <em>"Modified embedded atom method (meam) with bond order implementation in lammps"</em>, 6th LAMMPS Workshop and Symposium, Albuquerque, NM, August 2019.</li>
            <li> A. Bowman and Sungkwang Mun, <em>"Multi-threaded extension of meam force field in molecular dynamic simulations"</em>, HPCMP User Group Metting, Vicksburg, MS, May 2019.</li>
            <li> S. Ababtin, Sungkwang Mun, R. Carino, A. Bowman, M. Baskes, and M. Horstemeyer, <em>"Multi-scale interfacial characteristics of single wall carbon nanotube (swcnt) composites embedded within polyethylene (pe)"</em>, TMS 2019 Annual Meeting &amp; Exhibition, San Antonio, TX, March 2019.</li>
            <li> M. A. Murphy, R. Prabhu, M. F. Horstemeyer, L. N. Williams, Sungkwang Mun, and M. I. Baskes, <em>"Molecular dynamics simulations of neuronal membrane mechanoporation damage"</em>, International Mechanical Engineering Congress &amp; Exposition, Pheonix, AZ, November 2016.</li>
            <li> Sungkwang Mun, G. F. Sassenrath, Nayeon Lee, M. A. Murphy, J.Q. Corbitt, and R. Prabhu, <em>"Development of crop coefficients for scheduling irrigation of crops in humid environments"</em>, American Society of Agricultural and Biological Engineers Annual International Meeting, Orlando, FL, July 2016.</li>
            <li> A. Bakhtiary, A. E. Florence, M. A. Murphy, Sungkwang Mun, J. Liao, L. N. Williams, M. F. Horstemeyer, M. C. LaPlaca, and R. Prabhu, <em>"The stress rate dependency of intracellular calcium ion concentration in a neuronal membrane mechanoporation during mechanical insult"</em>, Summer Biomechanics, Bioengineering and Biotransport Conference, Snowbird, UT, June 2015.</li>
            <li> Michael A. Murphy, Sungkwang Mun, M. F. Horstemeyer, Steven R. Gwaltney, Tonya W. Stone, Michelle C. LaPlaca, Jun Liao, Lakiesha N. Williams, and R. Prabhu, <em>"Constructing rudimentary limit curves for neuronal phospholipid bilayer failure and theoretical calcium penetration"</em>, Summer Biomechanics, Bioengineering and Biotransport Conference, Snowbird, UT, June 2015.</li>
        </ol>
"""

content = content.replace('        <h3>Dissertation</h3>', software_and_pres_html + '\n        <h3>Dissertation</h3>')

with open('publications.html', 'w', encoding='utf-8') as f:
    f.write(content)
