import hashlib

class DrupalPasswordHasher():
    """
    >>> h = DrupalPasswordHasher()
    >>> h.verify("password1234", "$S$DeIZ1KTE.VzRvudZ5.xgOakipuMFrVyPmRdWTjAdYieWj27NMglI")
    True
    """
    
    DRUPAL_HASH_COUNT = 15
    DRUPAL_MIN_HASH_COUNT = 7
    DRUPAL_MAX_HASH_COUNT = 30
    DRUPAL_HASH_LENGTH = 55
    _ITOA64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    algorithm = 'drupal'
    
    def verify(self, password, hashed_password):
        hashed_password = hashed_password.replace('drupal','')

        setting = hashed_password[0:12]
        
        if setting[0] != '$' or setting[2] != '$':
            return False
            
        count_log2 = self._ITOA64.index(setting[3])
        
        if count_log2 < self.DRUPAL_MIN_HASH_COUNT or count_log2 > self.DRUPAL_MAX_HASH_COUNT:
            return False
  
        salt = setting[4:4+8]
        
        if len(salt) != 8:
            return False
        
        count = 2 ** count_log2
           
        pass_hash = hashlib.sha512(salt + password).digest()

        for _ in range(count):
            pass_hash = hashlib.sha512(pass_hash + password).digest()

        hash_length = len(pass_hash)

        output = setting + self._password_base64_encode(pass_hash, hash_length)
        
        if len(output) != 98:
            return False
        
        return output[:self.DRUPAL_HASH_LENGTH] == hashed_password      

    def safe_summary(self, encoded):
        algorithm, iterations, salt = encoded.split('$', 3)
        return SortedDict([
            ('algorithm', self.algorithm),
            ('iterations', iterations),
            ('salt', 'salt'),
            ('hash', 'hash'),
        ])


    def _password_base64_encode(self, to_encode, count):
        output = ''
        i = 0
        while True:
            value = ord(to_encode[i])
            
            i += 1
            
            output = output + self._ITOA64[value & 0x3f]
            if i < count:
                value |= ord(to_encode[i]) << 8
            output = output + self._ITOA64[(value >> 6) & 0x3f]
    
            if i >= count:
                break

            i += 1
    
            if i < count:
                value |= ord(to_encode[i]) << 16
            
            output = output + self._ITOA64[(value >> 12) & 0x3f]
    
            if i >= count:
                break
            
            i += 1
            
            output = output + self._ITOA64[(value >> 18) & 0x3f]
            
            if i >= count:
                break
        
        return output