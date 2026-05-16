with open('index.html', 'r') as f:
    content = f.read()

changes = 0
def patch(old, new, label):
    global content, changes
    if old in content:
        content = content.replace(old, new)
        print(f"OK {label}")
        changes += 1
    else:
        print(f"MISSING {label}")

# Fix colonnes tableau PDF
patch(
    "doc.text('DÉSIGNATION',ml+3,y+0.5);doc.text('P.U. HT',148,y+0.5,{align:'right'});doc.text('TOTAL HT',192,y+0.5,{align:'right'});y+=10;\n  (d.lignes||[]).forEach((l,i)=>{\n    if(i%2===1)rc(ml,y-4,W-ml-mr,8,[248,248,248]);\n    sf(8,'normal');const nl=doc.splitTextToSize(l.nom||'',108);doc.text(nl,ml+3,y+0.5);\n    sf(8,'normal',G);doc.text(`${(l.prix||0).toFixed(2)} \u20ac`,148,y+0.5,{align:'right'});\n    sf(8,'bold');doc.text(`${(l.prix||0).toFixed(2)} \u20ac`,192,y+0.5,{align:'right'});\n    y+=8*(nl.length>1?nl.length:1);\n  });",
    "doc.text('DÉSIGNATION',ml+3,y+0.5);doc.text('TOTAL HT',192,y+0.5,{align:'right'});y+=10;\n  (d.lignes||[]).forEach((l,i)=>{\n    if(i%2===1)rc(ml,y-4,W-ml-mr,8,[248,248,248]);\n    sf(8,'normal');const nl=doc.splitTextToSize(l.nom||'',155);doc.text(nl,ml+3,y+0.5);\n    sf(8,'bold');doc.text(`${(l.prix||0).toFixed(2)} \u20ac`,192,y+0.5,{align:'right'});\n    y+=8*(nl.length>1?nl.length:1);\n  });",
    "colonnes tableau"
)

# Fix bloc totaux
patch(
    "rc(122,y-2,70,10,[240,240,240]);sf(8,'normal',G);doc.text('Total HT',124,y+4.5);sf(9,'bold');doc.text(`${tot.toFixed(2)} \u20ac`,192,y+4.5,{align:'right'});y+=12;\n  rc(122,y-2,70,10,[240,240,240]);sf(8,'normal',G);doc.text('TVA',124,y+4.5);sf(8,'italic',G);doc.text('Non applicable (293B)',192,y+4.5,{align:'right'});y+=12;\n  rc(122,y-2,70,12);sf(8,'normal',[200,200,200]);doc.text('TOTAL TTC',124,y+5.5);sf(11,'bold',[255,255,255]);doc.text(`${tot.toFixed(2)} \u20ac`,192,y+5.5,{align:'right'});y+=18;",
    """// Totaux — tableau 2 colonnes aligné
  const tw=80,tx=ml; // largeur bloc total, x départ
  // Total HT
  doc.setFillColor(245,245,245);doc.rect(tx,y,W-ml-mr,9,'F');
  sf(8,'normal',G);doc.text('Total HT',tx+3,y+6);
  sf(9,'bold',K);doc.text(`${tot.toFixed(2)} \u20ac`,W-mr-3,y+6,{align:'right'});
  y+=11;
  // TVA
  doc.setFillColor(245,245,245);doc.rect(tx,y,W-ml-mr,9,'F');
  sf(8,'normal',G);doc.text('TVA',tx+3,y+6);
  sf(8,'italic',G);doc.text('Non applicable \u2014 art. 293B CGI',W-mr-3,y+6,{align:'right'});
  y+=11;
  // Total TTC
  rc(tx,y,W-ml-mr,12,DK);
  sf(9,'bold',[160,160,160]);doc.text('TOTAL TTC',tx+3,y+8);
  sf(13,'bold',[255,255,255]);doc.text(`${tot.toFixed(2)} \u20ac`,W-mr-3,y+8,{align:'right'});
  y+=18;""",
    "bloc totaux"
)

# Fix acompte
patch(
    "sf(7,'normal',G);doc.text('Confirme la date.',192,y+3.5,{align:'right'});y+=14;",
    "sf(7,'normal',G);doc.text('Confirme définitivement la date et la prestation.',W-mr-3,y+3.5,{align:'right'});y+=14;",
    "acompte texte"
)

with open('index.html', 'w') as f:
    f.write(content)
print(f"\n{changes} patch(es) appliqué(s)")
