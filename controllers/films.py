def liste_films():
    requete=db.films.id>0
    rows=db(requete).select()
    return response.render('films/liste_films.html', dict(films=rows))



def ajout_film():
    form = SQLFORM(db.films)
    if form.process().accepted:
        session.flash = "Le film a été ajouté avec succès !"
        redirect(URL('liste_films'))
    return response.render('films/formulaire.html', dict(form=form))
  
  
  
  
def modifier_film():
    film_id = request.args(0)
    film = db.films(film_id) or redirect(URL('liste_films'))
    form = SQLFORM(db.films, film, deletable=True, showid=False)
    if form.process().accepted:
        session.flash = 'Film modifié avec succès'
        redirect(URL('liste_films'))
        
    return response.render('films/formulaire.html', dict(form=form))
    
    
def supprimer_film():
    film_id = request.vars.id
    db(db.films.id == film_id).delete()
    redirect(URL('films', 'liste_films'))
    return response.render('films/liste_films.html')