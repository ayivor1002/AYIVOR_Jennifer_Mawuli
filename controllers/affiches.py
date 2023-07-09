def liste_affiches():
    requete=db.affiches.id>0
    rows=db(requete).select()
    return response.render('affiches/liste_affiches.html', dict(affiches=rows))



def ajout_affiche():
    form = SQLFORM(db.affiches)
    if form.process().accepted:
        session.flash = "L'affiche a été ajouté avec succès !"
        redirect(URL('liste_affiches'))
    return response.render('affiches/formulaire.html', dict(form=form))
  
  


def modifier_affiche():
    affiche_id = request.args(0)
    affiche = db.affiches(affiche_id) or redirect(URL('liste_affiches'))
    form = SQLFORM(db.affiches, affiche, deletable=True, showid=False)
    if form.process().accepted:
        session.flash = 'Affiche modifiée avec succès'
        redirect(URL('liste_affiches'))
        
    return response.render('affiches/formulaire.html', dict(form=form))
    
    
 
 
def supprimer_affiche():
    affiche_id = request.vars.id
    db(db.affiches.id == affiche_id).delete()
    redirect(URL('affiches', 'liste_affiches'))
    return response.render('affiches/liste_affiches.html')

