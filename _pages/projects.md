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
  <a href="#ao-fed-ifu">AO-fed IFU</a>
</nav>

<a id="adaptive-optics"></a>
<a id="adaptive-optics--basics"></a>

## Shack-Hartmann Wavefront Sensing & Adaptive Optics Simulation

<p class="project-role">Independent project · March 2026–present · Ongoing development</p>

In an astronomical instrumentation lab, I tuned a deformable mirror and observed how its shape changed the wavefront error. In my Python model I can follow the same correction one frame at a time. I propagate the light through a Shack–Hartmann lenslet array, measure the spot positions on a noisy detector, and use a calibrated interaction matrix to calculate the next mirror command.

I varied gain, delay and detector noise, then measured the residual wavefront, Strehl and encircled energy. The Explorer replays the recorded wavefronts and science images. I also compared selected optical calculations with analytic solutions and HCIPy.

<nav class="portfolio-jump" aria-label="AO project links">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/">Interactive explorer</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation">Source code</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/blob/main/docs/design-decisions.md">Design decisions</a>
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">Loss-of-lock case study</a>
</nav>

### Selected case study — diagnosing a closed-loop reconstruction failure

In the 2.2 m natural-guide-star model, reconstruction stopped at 0.981 s. As spots dropped out, weakly sensed modes produced large mirror commands and pushed more spots past the rejection threshold.

I raised the TSVD cutoff from 0.001 to 0.05 and repeated the run with the same atmosphere and calibration. All 1,500 frames reconstructed, the mirror stayed within its stroke limits, and the recovery safeguard stayed inactive. The two traces below come from a simulated Robo-AO-2-like configuration.

<figure class="project-case-figure">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">
    <img src="{{ '/images/projects/ngs-22m-comparison.png' | relative_url }}" alt="Recorded synthetic AO results: the original 2.2 m run loses usable reconstruction near one second, while stronger TSVD regularisation maintains reconstruction through the matched two-second trajectory; H-band Strehl, usable measurement rows and DM limits are shown" width="1760" height="1520" loading="lazy" decoding="async">
  </a>
  <figcaption>The two 2.2 m traces show the original and revised runs. The 2 m trace is a separate one-second reference.</figcaption>
</figure>

In a separate 2 m test, I used the same on-axis telescope geometry, atmosphere and loop gain in my model and in TIPTOP. At 1.65 µm the peak Strehl was 0.257–0.419 across three time-domain exposures. TIPTOP gave 0.710. In the first exposure, residual tilt accounted for 69% of the wavefront variance. [Comparison plot and settings](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/tree/main/docs/scao-comparison)

[Methods and numerical checks](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation#scope-and-evidence) · [Case configurations, diagnosis and limitations](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/tree/website/site/derived/ngs-22m-53663e0742d1d106)

### Comparing loop gains in the historical 42 m AO model

With three frames of delay, gain 0.2 applied a smaller fraction of each correction and softened the late rise in residual wavefront error in one run, while gain 0.3 left less error early on and gave a sharper image over the full 0.8 s exposure (peak Strehl 0.722 versus 0.674).

[Explore the 42 m gain comparison](https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#gain42)

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

<a id="ao-fed-ifu"></a>

## AO-fed integral-field spectrograph

I passed a synthetic source cube through an AO point-spread function, an image slicer, a spectrograph and a detector. Comparing the reconstructed cube with the input lets me measure what spatial and spectral information the instrument recovered.

[AO-fed IFU project and source code](https://github.com/xhvoid/AO-Fed-IFU-Spectrograph-Simulation)

[Education and laboratory experience]({{ '/experience/' | relative_url }}) · [CV]({{ '/cv/' | relative_url }})
