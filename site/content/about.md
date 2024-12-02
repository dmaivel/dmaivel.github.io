---
title: "About"
hasMath: false
_build:
  list: never
---

{{< marginnote ind="" >}} <img src="https://avatars.githubusercontent.com/u/38770072?v=4" onload="applyThemeToImage('pfp');" id="pfp" style="object-fit: cover; border-radius: 10%; width: 256px;" /> {{< /marginnote >}}
I am a self-taught programmer, interested in low level development. I am experienced in C/C++ and x86/64 assembly. If you would like to get to know more about my work, here are some of my projects:
- [**SharedGL**](https://github.com/dmaivel/sharedgl): An OpenGL implementation, allowing for 3D acceleration for Windows and Linux guests in QEMU through shared memory or over a network.
- [**covirt**](https://github.com/dmaivel/covirt): An x86-64 code virtualizer, protecting binaries via virtualization-based obfuscation, translating native instructions into a custom VM architecture.
- [**vscc**](https://github.com/dmaivel/vscc): An x86-64 JIT compiler backend, built with no third party dependencies. Includes an intermediate language and its own code generation.
  - [**pyvscc**](https://github.com/dmaivel/pyvscc): A proof of concept compiler frontend for `vscc`, capable of compiling basic python into x86-64 assembly.
- [**ntoseye**](https://github.com/dmaivel/ntoseye): Windows kernel debugger for Linux hosts running Windows under KVM/QEMU. Mimics the syntax/output of WinDbg.
- [**glBLAS**](https://github.com/dmaivel/glBLAS): A software library containing BLAS functions written in OpenGL fragment shaders, challenging the performance of cuBLAS *(on old GPUs)*.
- [**cugrad**](https://github.com/dmaivel/cugrad): An automatic differentiation library written in C++ and CUDA. All kernels are written from scratch.
- [**cml**](https://github.com/dmaivel/cml): An old project exploring deep feed forward neural networks.