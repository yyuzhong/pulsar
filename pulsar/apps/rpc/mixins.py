from pulsar import send

from .jsonrpc import JSONRPC


__all__ = ['PulsarServerCommands']


class PulsarServerCommands(JSONRPC):
    '''Some useful commands to add to your :class:`JSONRPC` handler to get you
started. It exposes the following functions:'''    
    def rpc_ping(self, request):
        '''Ping the server.'''
        return 'pong'
    
    def rpc_echo(self, request, message=''):
        '''Echo the server.'''
        return message
    
    def rpc_server_info(self, request):
        '''Return a dictionary of information regarding the server and workers.
It invokes the :meth:`extra_server_info` for adding custom information.'''
        info = yield send('arbiter', 'info')
        yield self.extra_server_info(request, info)
    
    def rpc_functions_list(self, request):
        '''List of (method name, method document) pair of all method exposed by
this :class:`JSONRPC` handler.'''
        return list(self.listFunctions())
    
    def rpc_documentation(self, request):
        '''Documentation in restructured text.'''
        return self.docs()
    
    def rpc_kill_actor(self, request, aid):
        '''Kill and actor which match the id *aid*.'''
        return send('arbiter', 'kill_actor', aid)
        
    def extra_server_info(self, request, info):
        '''Not an ``rpc`` method, but an internal method which adds additional
information to the info dictionary. Used by the :meth:`rpc_server_info`
method.'''
        return info
    
