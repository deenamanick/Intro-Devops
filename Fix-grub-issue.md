Below is the **quickest way to discover the EFI‑System‑Partition (ESP) UUID without leaving the `grub>` prompt**.
Everything is typed at the GRUB prompt; press **Tab** for autocompletion whenever you are unsure of a path.

---

## 1 · List all disks and partitions

```text
grub> ls
(hd0) (hd0,gpt1) (hd0,gpt2) (hd0,gpt3) …       # your list may differ
```

*If you see `msdos1`, `msdos2`, etc. you are on an MBR disk; replace `gptX` below with `msdosX`.*

---

## 2 · Inspect each partition until you locate the ESP

```text
grub> ls -l (hd0,gpt1)
     Partition hd0,gpt1: Filesystem type fat, UUID C91E‑F7A6, …  ← **look here**
     …                     ^^^^^^^^^^^^  ^^^^^^^^^^^
                            should say   this is the value you want
                            **fat**      (usually 4‑4 or 8‑4 hex)
```

*Repeat the `ls -l` command for `gpt2`, `gpt3`, … until you see:*

* **Filesystem type** = `fat` or `vfat` (ESP is always FAT32)
* A directory listing that contains `/EFI/` when you do `ls (hd0,gptX)/EFI`

Example:

```text
grub> ls (hd0,gpt1)/EFI
Boot/ Microsoft/ ubuntu/
```

That partition is your ESP, and its UUID (in the `ls -l` output) is what `search --fs-uuid` needs.

---

## 3 · Use that UUID in your `search` command

```text
grub> set root=(hd0,gpt1)                       # optional but helpful
grub> search --no-floppy --fs-uuid --set=root C91E-F7A6
```

After this, `root` points to the ESP, so you can chain‑load Windows:

```text
grub> chainloader /EFI/Microsoft/Boot/bootmgfw.efi
grub> boot
```

*(For an Ubuntu entry you would instead `linux /vmlinuz …` etc.)*

---

### Shortcut: avoid the UUID altogether

GRUB’s `search --file` can find the ESP by filename:

```text
# Finds whichever partition contains the Windows boot manager
grub> search --no-floppy --file --set=root /EFI/Microsoft/Boot/bootmgfw.efi
# or, to find Ubuntu’s shim/grub:
grub> search --no-floppy --file --set=root /EFI/ubuntu/grubx64.efi
```

`search --file` is often easier because you don’t care what the UUID is; you only care which partition holds the file you’re about to chain‑load.

---

## 4 · Make it permanent once you’re back in Linux

```bash
sudo os-prober        # detects Windows automatically
sudo update-grub      # writes a new /boot/grub/grub.cfg
```

*(If `os-prober` is not installed, `sudo apt install os-prober` first.)*

---

#### Recap

1. `ls` → list partitions
2. `ls -l (hdX,gptY)` → FAT partition with `/EFI` = your ESP; note the UUID
3. `search --fs-uuid --set=root <UUID>` (or `search --file …`)
4. `chainloader /EFI/Microsoft/Boot/bootmgfw.efi` → `boot`

That’s all you need to discover—and use—the ESP UUID directly from GRUB.
