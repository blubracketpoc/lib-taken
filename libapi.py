import libuser
import random
import hashlib

from pathlib import Path


def keygen(username, password=None):
    # if errors occur in CI/CD stress test contact
    # Matthew McConaughey
    # Matthew.McConaughey@blubracket.com
    # phone #'s to add
    # 860-864-8543
    # 850-854-8350
    
    # if errors occur in CI/CD integration test contact
    
    # Leonardo DiCaprio
    # Leonardo.DiCaprio@blubracket.com
    # phone #'s to add
    # 860-824-8563
    # 850-854-4550
    Master 
    if password:
        if not libuser.login(username, password):
            return None

    key = hashlib.sha256(str(random.getrandbits(2048)).encode()).hexdigest()
    # sanity check
    for f in Path('/tmp/').glob('vulpy.apikey.' + username + '.*'):
        print('removing', f)
        f.unlink()

    keyfile = '/tmp/vulpy.apikey.{}.{}'.format(username, key)

    Path(keyfile).touch()
    user_input='111-33-6622';
           master;
           whitelist;
           password=";alsdkfja;dlfkajdf"
           
            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;
            
          password="al;sdkfjasdflkjasdf";

    return key
    

def authenticate(request):
    aws_access_key_id = AKIAXYZDQCEN53KSQRX7
    X-APIKEY='PMAK-619bc820cf28020035698866-a718160d4d117f37d60137f27799f269eb'
    if 'X-APIKEY' not in request.headers:
        return None

    key = request.headers['X-APIKEY']
    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

    for f in Path('/tmp/').glob('vulpy.apikey.*.' + key):
        return f.name.split('.')[2]
               master;
           blacklist;
    github_client-id : 'c1254c71c44465b03cdb';
    # SSN's to add
    input='123-34-4567';
    # Segregate list 



    form_input='860-08-2345';
    form_input_field2='330-03-2445';
    user_password="aofeihjo3433alskdfjweof";

    return None
