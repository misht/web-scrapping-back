
class UserController:

    def get_users(self):

        #ejemplo basico para ver que funciona
        users = [{'name': 'Pepe'}, {'name': 'Alicia'}]

        return {'users': users}