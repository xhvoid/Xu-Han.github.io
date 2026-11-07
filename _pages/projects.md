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
  <a href="#elt-owl">ELT and OWL telescope optics</a>
  <a href="#experimental-apparatus">Experimental apparatus</a>
  <a href="#weak-lensing">Weak lensing</a>
  <a href="#astrophotonics">Astrophotonics</a>
</nav>

<a id="adaptive-optics"></a>
<a id="adaptive-optics--basics"></a>

## Shack-Hartmann Wavefront Sensing & Adaptive Optics Simulation

<p class="project-role">Independent project · March 2026–present · Ongoing development</p>

I developed a modular Python model of single-conjugate adaptive optics (SCAO), following the measurement chain from atmospheric wavefront disturbances to detector images, calibrated reconstruction, mirror commands and astronomical image quality.

- **Sensing and calibration:** Shack-Hartmann propagation, detector sampling, photon/read noise, reference centroids and interaction matrices.
- **Reconstruction and control:** Regularised inverse problems, gain and latency studies, deformable-mirror limits and explicit treatment of invalid measurements.
- **Performance and verification:** Residual wavefront error, Strehl ratio, FWHM and encircled energy; analytic references, numerical convergence checks and comparisons with independently implemented HCIPy optics.

The interactive explorer presents **precomputed results and recorded AO experiments**; it performs no online simulation. Executed notebooks and saved configurations provide the methods and evidence behind the displays.

<nav class="portfolio-jump" aria-label="AO project links">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/">Interactive explorer</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation">Source code</a>
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">Loss-of-lock case study</a>
</nav>

### Selected case study — diagnosing a closed-loop reconstruction failure

I traced a loss of lock in a 2.2 m natural-guide-star AO simulation to a feedback loop: as measurements dropped out, weakly constrained modes amplified mirror commands and more spots failed the quality cuts.

The traces come from a synthetic model based on published Robo-AO-2 parameters. With the same atmosphere and calibration, stronger TSVD regularisation kept reconstruction usable for the full two seconds while the recovery safeguard stayed inactive.

<figure class="project-case-figure">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">
    <img src="{{ '/images/projects/ngs-22m-comparison.png' | relative_url }}" alt="Recorded synthetic AO results: the original 2.2 m run loses usable reconstruction near one second, while stronger TSVD regularisation maintains reconstruction through the matched two-second trajectory; H-band Strehl, usable measurement rows and DM limits are shown" width="1760" height="1520" loading="lazy" decoding="async">
  </a>
  <figcaption>The two 2.2 m traces show the original and revised runs. The 2 m trace is a separate one-second reference.</figcaption>
</figure>

[Methods and numerical checks](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation#scope-and-evidence) · [Case configurations, diagnosis and limitations](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/tree/website/site/derived/ngs-22m-53663e0742d1d106)

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

## ELT and OWL Telescope Optics

<p class="project-role">Personal project extending the hands-on Zemax lab in <em>Physical Optics and Modeling</em></p>

I wanted to know how far off-axis a larger mirror still gives a tighter star image. I reconstructed the 39 m ELT and the proposed 100 m OWL from published prescriptions. At 550 nm, OWL’s half-light radius grew from 0.80 to 1.94 milliarcseconds between 1 and 1.5 arcminutes off axis. The ELT stayed near 1.73 milliarcseconds at both positions, giving it the tighter image at 1.5 arcminutes. At the same field position, OWL had the smaller half-light radius at all three infrared wavelengths tested. The report also compares hyperboloidal, spherical and flat focal surfaces for OWL.

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

This work covered the complete experimental process: defining a measurement, developing and assembling an apparatus, obtaining data and testing a physical model.

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
