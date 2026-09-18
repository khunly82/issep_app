from fastapi.params import Param
import sqlalchemy as sql
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from models.operateur import Operateur
from models.sessionFactory import session_factory
from models.sousTraitant import SousTraitant

app = FastAPI()

templates = Jinja2Templates(directory='views')

@app.get('/hello')
def hello():
    return 'hello world !!'

@app.get('/api')
def api():
    with session_factory() as session:
        query = sql.select(Operateur)
        return session.scalars(query).all()

@app.get('/ma-premiere-page-web')
def maPage(request: Request):
    return templates.TemplateResponse(
        request, 
        name='my-view.html',
    )

@app.get('/page1')
def page1(request: Request, selectedOperateur = Param(default=2)):
    # ouverture de la db access
    with session_factory() as session:
        # récupération des données Operateurs
        query = sql.select(Operateur).where(Operateur.OperateurActif == 1)
        operateurs = session.scalars(query).all()
        # récupération des données Soustraitants
        query = (sql.select(SousTraitant)
                 .where(SousTraitant.Actif == 1)
                 .where(SousTraitant.NumOperateur == selectedOperateur))
        sousTraitants = session.scalars(query).all()

        # création du template HTML
        return templates.TemplateResponse(
            request,
            name='page1.html',
            context={
                "operateurs": operateurs,
                "sousTraitants": sousTraitants,
                "selectedOperateur": int(selectedOperateur)
            }
        )

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)
