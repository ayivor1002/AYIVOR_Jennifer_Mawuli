@auth.requires_login()
def liste_reservations():
    requete=db.reservations.id>0
    rows=db(requete).select()
    return response.render('reservations/liste_reservations.html', dict(reservations=rows))



def ajout_reservation():
    form = SQLFORM(db.reservations)
    if form.process().accepted:
        session.flash = "La reservation a été ajoutée avec succès !"
        redirect(URL('liste_reservations'))
    return response.render('reservations/formulaire.html', dict(form=form))
 
 
 
def modifier_reservation():
    reservation_id = request.args(0)
    reservation = db.reservations(reservation_id) or redirect(URL('liste_reservations'))
    form = SQLFORM(db.reservations, reservation, deletable=True, showid=False)
    if form.process().accepted:
        session.flash = 'Reservation modifiée avec succès'
        redirect(URL('liste_reservations'))
        
    return response.render('reservations/formulaire.html', dict(form=form))
     
     
     
def supprimer_reservation():
    reservation_id = request.vars.id
    db(db.reservations.id == reservation_id).delete()
    redirect(URL('reservations', 'liste_reservations'))
    return response.render('reservations/liste_reservations.html')

