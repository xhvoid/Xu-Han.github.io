---
permalink: /projects/
title: "Research & engineering projects"
excerpt: "Adaptive optics, ELT and OWL telescope optics, experimental apparatus development and weak-lensing research."
author_profile: true
---

My projects range from telescope optics and adaptive optics simulations to an experimental charge-measurement apparatus and weak-lensing data analysis.

{% include portfolio-styles.html %}

<nav class="portfolio-jump" aria-label="Project sections">
  <a href="#adaptive-optics">Adaptive optics</a>
  <a href="#elt-owl">OWL optical reconstruction</a>
  <a href="#experimental-apparatus">Experimental apparatus</a>
  <a href="#weak-lensing">Weak lensing</a>
  <a href="#astrophotonics">Astrophotonics</a>
</nav>

### Laboratory Adaptive Optics — LMU Munich, 2022
{: #lmu-ao-lab}

In July 2022, I worked with an ALPAO bench in the Instrumental Astrophysics Laboratory at LMU Munich. We applied individual Zernike modes with the deformable mirror and measured the wavefront with a Shack–Hartmann sensor. We studied static correction, then introduced an artificial turbulence screen to investigate dynamic correction. We followed the wavefront error and Strehl ratio and examined the point-spread function (PSF) on the science camera.

<p class="project-role">Laboratory supervisor · Dr. Frank Grupp, USM / LMU Munich</p>

<details class="project-evidence">
  <summary>View laboratory images</summary>
  <figure>
    <img src="{{ '/images/projects/ao_bench_software.png' | relative_url }}" alt="ALPAO software showing the deformable mirror controls, measured wavefront, correction history and science-camera view" width="1173" height="605" loading="lazy">
    <figcaption>The ALPAO controls let us follow the measured wavefront and correction history alongside the science-camera image.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/images/projects/ao_bench_turbulence.jpg' | relative_url }}" alt="Open-loop PSF with several bright lobes on the left and closed-loop PSF with a more concentrated core on the right" width="1056" height="576" loading="lazy">
    <figcaption>Science-camera PSFs with artificial turbulence. The loop is open on the left and closed on the right. Both panels use the same intensity mapping.</figcaption>
  </figure>
</details>

<a id="adaptive-optics"></a>
<a id="adaptive-optics--basics"></a>

## Shack-Hartmann Wavefront Sensing & Adaptive Optics Simulation

<p class="project-role">Independent project · March 2026–present · Ongoing development</p>

The LMU bench was my first hands-on experience with adaptive optics. In 2026 I started a Python model so I could follow the correction from a shift in a detector spot to the next mirror command. I propagate light through a Shack–Hartmann lenslet array and measure spot centroids in the presence of photon noise and detector read noise. In the 2.2 m case, I reconstruct the correction using a truncated singular value decomposition (TSVD) of the calibrated interaction matrix. The 42 m replay uses damped least squares.

I varied gain, delay and detector noise, then measured the residual wavefront error, Strehl and encircled energy. In a layered atmosphere I also examined how well the on-axis correction worked for a science target farther from the guide star. The Explorer replays the recorded wavefronts and science images. I compared selected optical calculations with analytic solutions and HCIPy.

<nav class="portfolio-jump" aria-label="AO project links">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/">Interactive explorer</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation">Source code</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/blob/main/docs/design-decisions.md">Design decisions</a>
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">Loss-of-lock case study</a>
</nav>

### Where did the four spots in the 42 m image come from?

Four faint spots in my simulated 42 m telescope image lay 0.45 arcseconds from the star along each axis. At 2.2 µm, a checkerboard pattern on a mirror with actuators spaced 0.5 m apart would send light to those positions. The simulated wavefront sensor registered this *waffle* pattern only weakly.

I filtered 96 checkerboard modes out of the mirror updates. On a replay of the same atmosphere, the average light at the four positions fell from 10.8 to 0.91 times the surrounding halo. I fixed the cutoff before testing three more realizations of the same system. All three met the image-quality and loop-operation criteria I had set in advance.

<figure class="project-case-figure">
  <img src="{{ '/images/projects/waffle-42m-fields.png' | relative_url }}"
       width="1400" height="650" loading="lazy" decoding="async"
       alt="Four circled diagonal spots are visible around the simulated star on the left. At the same positions on the right, no distinct spots stand out.">
  <figcaption>Before filtering (left) and after filtering (right). Both mean images show the same simulated atmosphere at 2.2 µm on a shared logarithmic scale. Peak Strehl rose from 0.754 to 0.767.
    <a href="{{ '/images/projects/waffle-42m-corner-spots.png' | relative_url }}">Enlarge the figure with upper-right corner views.</a>
    The zooms share a narrower intensity range. The ratios beneath them give the average light in all four marked regions relative to the halo at the same distance from the star.
  </figcaption>
</figure>

[See the spot positions, filter comparison and held-out results in AO Explorer →](https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#waffle42)

### Keeping the 2.2 m loop locked

In a 2.2 m simulation, rejected spot measurements drove the mirror to larger commands until reconstruction stopped at 0.981 s. I raised the reconstruction cutoff and replayed the same atmosphere. The revised loop reconstructed all 1,500 frames, and the mirror stayed within its stroke limits. [See the two loop traces.](https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22)

In a separate [42 m gain comparison](https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#gain42), lower gain softened a late residual excursion, while higher gain gave the sharper image over the full exposure.

For the separate multi-conjugate AO study, I used a frequency-domain model. I added a high-frequency fitting term to the TIPTOP/P3 residual spectrum and calculated the long-exposure PSF with MASTSEL.

<section class="project-evidence" aria-labelledby="ao-explorer-preview">
  <h3 id="ao-explorer-preview">AO correction in motion</h3>
  <div class="ao-preview-layout">
    <figure class="ao-preview-media">
      <input type="checkbox" id="ao-preview-still" class="ao-preview-toggle">
      <label for="ao-preview-still">Show still image</label>
      <div class="ao-preview-images">
        <picture class="ao-preview-animation">
          <source media="(prefers-reduced-motion: reduce)" srcset="{{ '/images/projects/ao-galaxy-comparison-poster.png' | relative_url }}">
          <img src="{{ '/images/projects/ao-galaxy-comparison.gif' | relative_url }}" alt="Animated comparison of NGC 1705 with uncorrected and AO-corrected simulated PSFs, with synchronized instantaneous PSF Strehl values at 1.65 micrometres, original frame numbers and simulated time" width="600" height="480" loading="lazy" decoding="async">
        </picture>
        <img class="ao-preview-poster" src="{{ '/images/projects/ao-galaxy-comparison-poster.png' | relative_url }}" alt="Still comparison at simulated time 0.200 seconds, with the corresponding uncorrected and AO-corrected PSF Strehl values" width="600" height="480" loading="lazy" decoding="async">
      </div>
      <figcaption>A recorded 2 m model: the same HST/F814W template through uncorrected and AO-corrected simulated PSFs, on one fixed brightness scale. Strehl readouts describe the corresponding 1.65 μm PSFs. One simulated second is replayed over 20 seconds; the loop repeats the same 126 recorded samples.</figcaption>
    </figure>
    <div class="ao-preview-more">
      <h4>Explore the full experiment</h4>
      <p>Replay the wavefronts and images, compare recorded cases, and inspect performance curves, methods and model limitations in the interactive explorer.</p>
      <div class="portfolio-actions">
        <a class="btn btn--primary" href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#galaxy-panel">Open AO Explorer</a>
      </div>
      <p class="ao-preview-credit">Template: HST/WFC3 F814W, LEGUS (GO-13364), via MAST. This mock observation retains the template’s resolution and residual noise; no additional image noise is added.</p>
    </div>
  </div>
</section>

<a id="elt-owl"></a>

## Reconstructing OWL and tracing an ensquared-energy discrepancy

I rebuilt OWL in Zemax from the prescription in ESO’s Blue Book. At 5 arcmin off axis, I obtained 1.472 µm total RMS wavefront error. ESO gives 1.476 µm. At 3 arcmin, however, my model put 77.1% of the light inside a square of half-width 50 µm at 2.2 µm. I read about 49.9% from ESO’s curve.

I kept the radius fixed and changed only the focal-surface conic from −1.295298 to zero. The result fell to 50.0%. Across the 101 sampled half-widths, the spherical-surface curve agreed with my readings of the ESO figure to about 0.4 percentage points. ESO does not specify the focal surface used for that figure.

<nav class="portfolio-jump" aria-label="Telescope optics report">
  <a href="{{ '/projects/elt-owl/' | relative_url }}">Read the engineering report</a>
</nav>

<a id="experimental-apparatus"></a>

## Experimental Collisional Charging Apparatus

<p class="project-role">B.Sc. Physics thesis · University of Duisburg-Essen · March–August 2021</p>

**Thesis:** *Design of an Experimental Setup for the Measurement of Collisional Charging on Granulate.*

I designed and built an apparatus to investigate charging in granular materials. The experiment tested a hypothesis concerning dust growth through collisions during the early stages of planet formation.

- Designed the mechanical components in CAD and fabricated prototype parts by 3D printing.
- Assembled the apparatus and integrated and debugged its electronic charge-measurement modules.
- Conducted experiments, analysed the grain-size dependence of charging and interpreted the measurements in relation to the physical hypothesis.

<figure class="project-case-figure">
  <img src="{{ '/images/projects/granulate-apparatus-cad.png' | relative_url }}" width="780" height="693" alt="CAD cutaway showing the grain reservoir, lid, voice coil and copper collecting cup" loading="lazy">
  <figcaption>The voice coil shakes the reservoir. A grain falls through the opening in the bottom of the reservoir into the copper cup, where I measure its charge. From Fig. 6 of my physics thesis.</figcaption>
</figure>
<figure class="project-case-figure">
  <img src="{{ '/images/projects/granulate-apparatus.jpg' | relative_url }}" width="1200" height="900" alt="Assembled shaker and charge-measurement electronics inside a metal shielding cylinder" loading="lazy">
  <figcaption>The assembled apparatus. I put the shaker and charge readout inside a metal cylinder to reduce electrical interference. From Fig. 8 of my physics thesis.</figcaption>
</figure>

**Supervisors:** Prof. Gerhard Wurm and Dr. Felix Jungmann.

<a id="weak-lensing"></a>
<a id="2d-voids"></a>

## Weak Lensing Void Finder

<p class="project-role">M.Sc. Astrophysics thesis · LMU Munich · March 2023–August 2024</p>

**Thesis:** *Watershed Cosmic Void Finder for Weak Gravitational Lensing Voids on 2D Full-Sky Convergence Maps.*

I developed a watershed algorithm for detecting cosmic voids in full-sky convergence maps and worked with Dark Energy Survey Year 3 (DES Y3) weak-lensing maps.

- Implemented void detection and studied the influence of algorithm parameters on the recovered populations.
- Characterised void abundance, effective radii, ellipticities and convergence profiles.

**Supervisors:** Prof. Joseph Mohr and Dr. Chris Davies.

[Thesis (PDF)]({{ '/files/watershed-voids-thesis.pdf' | relative_url }}) · [2D-Voids repository](https://github.com/xhvoid/2D-Voids)

<a id="additional-independent-projects"></a>

## Astrophotonics

A conceptual Python study linking residual AO wavefront error, injection jitter and photonic-lantern mode count to fibre coupling, spectral signal-to-noise ratio and radial-velocity precision. It connects complex-field propagation and modal overlap to a synthetic spectroscopic measurement.

**Methods:** Wave optics, coherent modal coupling, noise budgets and parameter studies.

[Repository](https://github.com/xhvoid/Astrophotonics) · [Executed notebook](https://github.com/xhvoid/Astrophotonics/blob/main/notebooks/eso_astrophotonics_showcase.ipynb)

[Education and laboratory experience]({{ '/experience/' | relative_url }}) · [CV]({{ '/cv/' | relative_url }})
